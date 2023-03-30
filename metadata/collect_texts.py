import os
import warnings
from metadata.collect_files import filenames_for_genre, list_genres
from metadata.parse import parse_metadata
from vtt.parse_vtt import parse_vtt, flatmap
from vtt.filter_metatext import filter_metatext

def collect_genres(metadata_file):
    metadata = parse_metadata(metadata_file)
    return list_genres(metadata)

def text_per_genre(metadata_file, data_directory):
    '''Returns a generator with the complete string of text for each genre.'''
    metadata = list(parse_metadata(metadata_file))
    genres = collect_genres(metadata_file)

    return (
        text_for_genre(data_directory, metadata, genre, subgenre)
        for genre, subgenre in genres
    )

def filter_existing_files(paths):
    '''
    Given a list of paths, filters out files that do not exist.
    Makes a warning for each file that does not exist.
    '''

    for path in paths:
        if os.path.exists(path):
            yield path
        # else:
        #     warnings.warn(f'File not found: {path}', Warning)

def text_for_genre(data_directory, metadata, genre, subgenre):
    '''Returns all the text for a genre as a single string.
    
    Uses the given `metadata` to select files in `data_directory` that match
    the given genre and subgenre.'''

    files = filenames_for_genre(metadata, genre, subgenre)
    paths = (os.path.join(data_directory, file) for file in files)
    real_paths = filter_existing_files(paths)

    lines = flatmap(parse_vtt, real_paths)
    filtered_lines = filter_metatext(lines)

    return '\n'.join(filtered_lines)