import re

def split_genre(genre_full):
    '''Split a name like "Informatief - Nieuws" into its components'''
    sep = r' [-–] '
    if len(re.findall(sep, genre_full)) == 1:
        return tuple(re.split(sep, genre_full))
    else:
        return genre_full, None
