import csv
import os
import click
from metadata.collect_texts import collect_genres, text_per_genre
from metadata.summary import find_metadata_file
from analysis.count import make_vectoriser
from analysis.lemmatize import Lemmatizer

def collect_token_counts(metadata_file, data_directory, lemmatizer=None):
    '''
    Collect token counts per genre.

    Input:
    - path to the metadata file
    - path to the directory containing VTT subtitle files
    - `lemmatizer` (default None): lemmatisation method. Either `None`, `'frog'`, or `'spacy'`
    
    Returns a tuple of the following:
    - a list of genres. Each genre is a tuple of genre/subgenre.
    - a list of the term in the vocabulary.
    - a matrix of term frequencies per genres. m[i,j] gives the frequency
    for genre i and term j in the aforementioned lists.
    '''
    genres = collect_genres(metadata_file)

    texts = text_per_genre(metadata_file, data_directory)

    if lemmatizer in ['spacy', 'frog']:
        lemmatizer = Lemmatizer(lemmatizer)
        processed = (lemmatizer.process(text) for text in texts)
    else:
        processed = texts

    cv, tdm = make_vectoriser(processed)
    vocab = list(cv.get_feature_names_out())

    return genres, vocab, tdm

def format_genre(genre_tuple):
    return ' - '.join(genre_tuple)

def save_counts(csv_path, genres, vocab, tdm):
    '''
    Save token counts per genre to a csv file.
    '''

    with open(csv_path, 'w') as outfile:
        formatted_genres = list(map(format_genre, genres))
        writer = csv.DictWriter(outfile, fieldnames = ['Term'] + formatted_genres)
        writer.writeheader()

        for i, term in enumerate(vocab):
            frequencies = {genre: tdm[j,i] for (j, genre) in enumerate(formatted_genres)}
            data = {'Term': term, **frequencies}
            writer.writerow(data)


def collect_and_save_counts(metadata_file, data_directory, output_file, lemmatizer=None):
    counts = collect_token_counts(metadata_file, data_directory, lemmatizer)
    save_counts(output_file, *counts)
    print('Done! Output file in {}'.format(os.path.abspath(output_file)))

# CLI


here = os.path.dirname(__file__)
data_dir = os.path.normpath(os.path.join(here, '..', 'data'))

vtt_dir_default = os.path.join(data_dir, 'NPO_vtt_dataset')
metadata_file_default = find_metadata_file()
output_file_default = os.path.join(data_dir, '..', 'token_frequencies.csv')


@click.command()
@click.argument(
    'metadata_file',
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    default=metadata_file_default,
)
@click.argument(
    'vtt_dir',
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default=vtt_dir_default,
)
@click.option(
    '--output',
    type=click.Path(),
    default=output_file_default,
)
@click.option(
    '--lemmatizer',
    type=click.Choice(['frog', 'spacy'])
)
def run(metadata_file, vtt_dir, output, lemmatizer):
    collect_and_save_counts(metadata_file, vtt_dir, output, lemmatizer)


if __name__ == '__main__':
    run()
