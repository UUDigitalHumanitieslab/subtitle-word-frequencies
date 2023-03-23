import pytest

from metadata.parse import parse
from metadata.collect import filenames_for_genre

files_per_genre = {
    ('Informatief', 'Nieuws/actualiteiten'): [
        'TEST-ZENDER0123456789.vtt',
        'TOETS-ZENDER0858694839.vtt',
    ],
    ('Informatief', 'Spel/quiz'): [
        'TESTEN-ZENDER04840389494.vtt'
    ],
    ('Informatief', None): [
        'TEST-ZENDER0123456789.vtt',
        'TOETS-ZENDER0858694839.vtt',
        'TESTEN-ZENDER04840389494.vtt',    
    ]
}

@pytest.mark.parametrize('genre,subgenre', files_per_genre.keys())
def test_filenames_for_genre(genre, subgenre, metadata_filename):
    metadata = parse(metadata_filename)
    filenames = filenames_for_genre(metadata, genre, subgenre)
    assert list(filenames) == files_per_genre[(genre, subgenre)]