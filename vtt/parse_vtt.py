import re

def parse_vtt(filename):
    '''Parses a .vtt subtitles file.
    
    Input should the the path to the file.
    
    Output is a generator that generates each line of the subtitles as a string.'''

    with open(filename) as f:
        content = f.read()
    
    timeframes = split_timeframes(content)
    return map(text_from_timeframe, timeframes)

# regular expressions
timestamp = r'\d{2}:\d{2}:\d{2}.\d+'
timewindow = rf'{timestamp} --> {timestamp}'
styling = r'( \w+:\S+)*'
timestamp_line = rf'{timewindow}{styling}'

content_line = r'\S[\S ]*'
additional_lines = rf'(\n{content_line})*'

timeframe = rf'{timestamp_line}\n{content_line}{additional_lines}'

opening_tag = r'<\w+(\.\w+)?>'
closing_tag = r'<\/\w+>'

segment = rf'{opening_tag}(.+?){closing_tag}' # use .+? to match anything in between the tags, but ungreedy (i.e. don't skip to the next tag)

def find_all_strings(pattern, string):
    '''
    Returns a generator of substrings in `string` that match `pattern`.
    
    Similar to re.findall but does not return tuples when the 
    pattern contains capturing groups
    '''

    for match in re.finditer(pattern, string):
        yield match.group(0)

def flatmap(function, collection):
    return (mapped_item for item in collection for mapped_item in function(item))

def split_timeframes(content):
    '''Split the string content of a file into parts for time segments'''
    return find_all_strings(timeframe, content)

def lines_from_timeframe(timeframe):
    lines = timeframe.split('\n')
    return lines[1:] #ignore line with the timestamp

def segments_from_line(line):
    '''Generate all text segments in a line, ignoring tags.'''
    if re.search(segment, line):
        for match in re.finditer(segment, line):
            yield match.group(2)
    else:
        yield line

def text_from_timeframe(timeframe):
    '''Get flat text from a timeframe segment.'''
    lines = lines_from_timeframe(timeframe)
    segments = flatmap(segments_from_line, lines)
    return '\n'.join(segments)