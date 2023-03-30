import csv
from metadata.collect_texts import collect_genres, text_per_genre
from analysis.count import make_vectoriser

def collect_token_counts(metadata_file, data_directory):
    '''
    Collect token counts per genre.
    
    Returns a tuple of the followin:
    - a list of genres. Each genre is a tuple of genre/subgenre.
    - a list of the term in the vocabulary.
    - a matrix of term frequencies per genres. m[i,j] gives the frequency
    for genre i and term j in the aforementioned lists.
    '''
    genres = collect_genres(metadata_file)

    texts = text_per_genre(metadata_file, data_directory)
    cv, tdm = make_vectoriser(texts)
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
