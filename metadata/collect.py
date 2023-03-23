from metadata.genres import split_genre

def filenames_for_genre(metadata, genre, subgenre = None):
    for row in metadata:
        if match_genre(row, genre, subgenre):
            yield row['guci'] + '.vtt'

def match_genre(metadata_row, genre, subgenre = None):
    row_genre, row_subgenre = split_genre(metadata_row['category'])
    
    if subgenre:
        return row_genre == genre and row_subgenre == subgenre
    else:
        return row_genre == genre