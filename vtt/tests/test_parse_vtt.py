import os
from vtt.parse_vtt import parse_vtt

test_file = os.path.join(os.path.dirname(__file__), 'test_data', 'test.vtt')

def test_parse_vtt():
    lines = list(parse_vtt(test_file))

    expected_lines = 10
    expected = [
        '888',
        '\n'.join(['Bla bla.', 'Bla bla?', 'Bla.']),
        '\n'.join(['Bla bla bla.', 'Bla!', 'Bla bla!']),
        # ... etc
    ]

    assert len(lines) == expected_lines
    for line, expected_line in zip(lines, expected):
        assert line == expected_line
