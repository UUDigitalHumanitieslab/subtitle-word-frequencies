from metadata.collect_texts import collect_genres, text_per_genre
from analysis.count import make_vectoriser

def collect_token_counts(metadata_file, data_directory):
    genres = collect_genres(metadata_file)

    texts = text_per_genre(metadata_file, data_directory)
    cv, tdm = make_vectoriser(texts)
    vocab = list(cv.get_feature_names_out())

    return genres, vocab, tdm