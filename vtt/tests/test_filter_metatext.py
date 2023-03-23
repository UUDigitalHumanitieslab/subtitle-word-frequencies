from vtt.filter_metatext import filter_metatext, is_metatext
from vtt.parse_vtt import parse_vtt
from vtt.tests.test_parse_vtt import test_file
import pytest

def test_filter_metatext():
    lines = list(parse_vtt(test_file))
    filtered = list(filter_metatext(lines))

    assert len(filtered) == len(lines) - 1

cases = {
    '888': True,
    'LIVEPROGRAMMA, ONDERTITELING KAN ACHTERLOPEN': True,
    '(muziek)': True,
    'Muziek!': False,
    'APPLAUS EN GEJUICH': True,
}

@pytest.mark.parametrize('fragment', cases.keys())
def test_is_metatext(fragment):
    assert is_metatext(fragment) == cases[fragment]