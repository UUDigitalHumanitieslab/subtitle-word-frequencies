import csv
import os
import click
from metadata.summary import find_metadata_file
from analysis.count import make_vectoriser, total_frequencies
from vtt.convert_to_plain import PLAIN_EXTENSION
from analysis.lemmatize import LEMMAS_EXTENSION

def iterate_files(directory, level='word'):
    suffix = LEMMAS_EXTENSION if level == 'lemma' else PLAIN_EXTENSION
    
    return (
        os.path.join(directory, filename)   
        for filename in os.listdir(directory)
        if filename.endswith(suffix)
    )

def get_content(filename):
    with open(filename) as f:
        return f.read()

def collect_token_counts(data_directory, level='word'):
    '''
    Collect token counts per genre.

    Input:
    - path to the directory containing pre-processed plain-text files
    - level: either `'word'` or `'lemma'`. Determines the selection of files
    
    Returns a list of `(term, frequency)` tuples, each giving the absolute
    frequency of a term.
    '''

    files = iterate_files(data_directory, level)
    texts = map(get_content, files)

    cv, tdm = make_vectoriser(texts)
    vocab = list(cv.get_feature_names_out())
    frequencies = total_frequencies(tdm)

    return list(zip(vocab, frequencies))


def format_genre(genre_tuple):
    return ' - '.join(genre_tuple)

def save_counts(csv_path, term_frequencies):
    '''
    Save token counts per genre to a csv file.
    '''

    with open(csv_path, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames = ['Term', 'Count'])
        writer.writeheader()

        for term, freq in term_frequencies:
            data = {'Term': term, 'Count': freq}
            writer.writerow(data)


def collect_and_save_counts(data_directory, output_file, level='word'):
    counts = collect_token_counts(data_directory, level)
    save_counts(output_file, counts)
    print('Done! Output file in {}'.format(os.path.abspath(output_file)))

# CLI


here = os.path.dirname(__file__)
data_dir = os.path.normpath(os.path.join(here, '..', 'data'))

vtt_dir_default = os.path.join(data_dir, 'NPO_vtt_dataset')
output_file_default = os.path.join(data_dir, '..', 'token_frequencies.csv')


@click.command()
@click.argument(
    'directory',
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default=vtt_dir_default,
)
@click.option(
    '--output',
    type=click.Path(),
    default=output_file_default,
)
@click.option(
    '--level',
    type=click.Choice(['word', 'lemma']),
    default='word',
)
def run(directory, output, level):
    collect_and_save_counts(directory, output, level)


if __name__ == '__main__':
    run()
