import os
import shutil
import pytest

from vtt.convert_to_plain import export_plain_text


@pytest.fixture()
def test_file(tmpdir):
    source = os.path.join(os.path.dirname(__file__), 'test_data', 'test.vtt')
    target = os.path.join(tmpdir, 'test.vtt')
    shutil.copyfile(source, target)
    return target


def test_export_plain_text(test_file):
    result_path = export_plain_text(test_file)
    assert result_path.endswith('/test.plain.txt')

    with open(result_path) as result:
        text = result.read()
        assert text.startswith('Bla bla.\nBla bla?\nBla.\nBla bla bla.')
