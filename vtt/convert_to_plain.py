import os
import click

from .parse_vtt import parse_vtt
from .filter_metatext import filter_metatext

PLAIN_EXTENSION = '.plain.txt'

def export_plain_text(vtt_filename):
    '''
    Export a plain text version of a .vtt subtitle file

    Applies `filter_metatext` to filter out non-utterances.
    
    Saves the output of `{x}/{y}.vtt` in `{x}/{y}.plain.txt`,
    with one line per utterance.
    '''

    lines = parse_vtt(vtt_filename)
    filtered_lines = filter_metatext(lines)

    output_filename = replace_suffix(vtt_filename, '.vtt', PLAIN_EXTENSION)

    with open(output_filename, 'w') as outfile:
        for line in filtered_lines:
            outfile.write(line)
            outfile.write('\n')
    
    return output_filename

def list_vtt_files(directory):
    '''
    Return the path of every .vtt file in a directory
    '''
    return list_files_with_suffix(directory, '.vtt')

def list_plain_text_files(directory):
    '''
    Return the path of every .plain.txt file in a directory
    '''
    return list_files_with_suffix(directory, PLAIN_EXTENSION)

def replace_suffix(filename, old, new):
    name = filename.removesuffix(old)
    output_filename = name + new
    return output_filename

def list_files_with_suffix(directory, suffix):
    '''
    Return the path of every file in a directory of which the name ends in `suffix`

    Not recursive: lists only direct children. Returns filepaths.
    '''
    
    files = filter(
        lambda filename: filename.endswith(suffix),
        os.listdir(directory)
    )
    paths = map(
        lambda filename: os.path.join(directory, filename),
        files,
    )
    return list(paths)

@click.command()
@click.argument(
    'vtt_dir',
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
)
def run(vtt_dir): 
    filepaths = list_vtt_files(vtt_dir)

    if not filepaths:
        print('No .vtt files found in directory')
        return

    for path in filepaths:
        export_plain_text(path)
    
    print('Done converting files')


if __name__ == '__main__':
    run()
