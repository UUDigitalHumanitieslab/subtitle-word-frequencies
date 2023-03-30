import os
from metadata.collect_files import filenames_for_genre, list_genres
from metadata.parse import parse_metadata
from vtt.parse_vtt import parse_vtt, flatmap
from vtt.filter_metatext import filter_metatext

def collect_genres(metadata_file):
    metadata = parse_metadata(metadata_file)
    return list_genres(metadata)

def text_per_genre(metadata_file, data_directory):
    '''Returns a dict with the complete string of text for each genre.'''
    metadata = list(parse_metadata(metadata_file))
    genres = collect_genres(metadata_file)

    return {
        (genre, subgenre):
            text_for_genre(data_directory, metadata, genre, subgenre)
        for genre, subgenre in genres
    }

def text_for_genre(data_directory, metadata, genre, subgenre):
    '''Returns all the text for a genre as a single string.
    
    Uses the given `metadata` to select files in `data_directory` that match
    the given genre and subgenre.'''

    files = filenames_for_genre(metadata, genre, subgenre)
    paths = [os.path.join(data_directory, file) for file in files]
    print(paths)

    lines = flatmap(parse_vtt, paths)
    filtered_lines = filter_metatext(lines)

    return '\n'.join(filtered_lines)