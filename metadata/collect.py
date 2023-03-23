from metadata.genres import split_genre

def collect_files_for_genre(directory, metadata, genre, subgenre = None):
    return []

def filenames_for_genre(metadata, genre, subgenre = None):
    for row in metadata:
        if match_genre(row, genre, subgenre):
            yield row['guci']

def match_genre(metadata_row, genre, subgenre = None):
    row_genre, row_subgenre = split_genre(metadata_row['category'])
    
    if subgenre:
        return row_genre == genre and row_subgenre == subgenre
    else:
        return row_genre == genre