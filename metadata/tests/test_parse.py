import os
from datetime import datetime

from metadata.parse import parse


def test_parse(metadata_filename):
    parsed = list(parse(metadata_filename))

    assert len(parsed) == 3

    expected_row = {
        'guci': 'TEST-ZENDER0123456789',
        'series_title': 'Testserie',
        'program_title': 'Testuitzending',
        'program_duration': 30,
        'department': 'ZENDER',
        'channel': 'NED1',
        'subtitle_type': 'prep',
        'date_publication': datetime(year=2022, month=12, day=31, hour=23, minute=59),
        'category': 'Informatief - Nieuws/actualiteiten'
    }

    assert parsed[0] == expected_row
