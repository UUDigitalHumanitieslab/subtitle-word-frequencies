import os
import click

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

def list_vtt_files(directory):
    '''
    Return the path of every .vtt file in a directory

    Returns a list of paths (strings). Not recursive: only lists direct children
    '''
    
    files = filter(
        lambda filename: filename.endswith('.vtt'),
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
