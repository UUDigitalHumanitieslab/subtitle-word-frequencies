import os
import pytest

here = os.path.dirname(__file__)

@pytest.fixture()
def metadata_filename():
    return os.path.join(here, 'tests/testdata/Word_frequency_qry.xlsx')

@pytest.fixture()
def data_directory():
    return os.path.abspath(here + '/tests/testdata/files')