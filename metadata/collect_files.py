from metadata.genres import split_genre

def list_genres(metadata):
    categories = filter(None, (row['category'] for row in metadata))
    genres = set(map(split_genre, categories))
    return list(sorted(genres))

def filenames_for_genre(metadata, genre, subgenre = None):
    for row in metadata:
        if match_genre(row, genre, subgenre):
            if row['guci']:
                yield row['guci'] + '.vtt'

def match_genre(metadata_row, genre, subgenre = None):
    if not metadata_row['category']:
        return False

    row_genre, row_subgenre = split_genre(metadata_row['category'])
    
    if subgenre:
        return row_genre == genre and row_subgenre == subgenre
    else:
        return row_genre == genre