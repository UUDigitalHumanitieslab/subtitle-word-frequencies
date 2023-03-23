import os
import pytest

@pytest.fixture()
def metadata_filename():
    here = os.path.dirname(__file__)
    return os.path.join(here, 'tests/testdata/Word_frequency_qry.xlsx')
