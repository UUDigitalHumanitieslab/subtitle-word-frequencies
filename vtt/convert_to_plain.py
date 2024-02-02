import os

from .parse_vtt import parse_vtt
from .filter_metatext import filter_metatext

def export_plain_text(vtt_filename):
    '''
    Export a plain text version of a .vtt subtitle file

    Applies `filter_metatext` to filter out non-utterances.
    
    Saves the output of `{x}/{y}.vtt` in `{x}/{y}.plain.txt`,
    with one line per utterance.
    '''

    lines = parse_vtt(vtt_filename)
    filtered_lines = filter_metatext(lines)

    name, _ext = os.path.splitext(vtt_filename)
    output_filename = name + '.plain.txt'

    with open(output_filename, 'w') as outfile:
        outfile.writelines(filtered_lines)
    
    return output_filename