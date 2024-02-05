import os
import pytest

here = os.path.dirname(__file__)

@pytest.fixture()
def data_directory():
    return os.path.abspath(here + '/tests/testdata/')