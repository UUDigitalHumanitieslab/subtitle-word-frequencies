import sys
import csv
import os
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

def collect_and_save_counts(metadata_file, data_directory, output_file):
    if not os.path.isfile(metadata_file):
        print('Metadatafile {} does not exist!'.format(metadata_file))
    elif not os.path.isdir(data_directory):
        print('Data directory {} does not exist!'.format(data_directory))
    else:
        counts = collect_token_counts(metadata_file, data_directory)
        save_counts(output_file, *counts)
        print('Done! Output file in {}'.format(os.path.abspath(output_file)))

if __name__ == '__main__':
    if len(sys.argv) == 4:
        metadata_file, data_dir, output_file = sys.argv[1:]
    else:
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'NPO_vtt_dataset')
        metadata_file = find_metadata_file()
        output_file = os.path.join(data_dir, '..', 'token_frequencies.csv')
        
    collect_and_save_counts(metadata_file, data_dir, output_file)