import pytest

from utils.helper import create_main_dataframe


def test_create_main_dataframe():
    df = create_main_dataframe()

    assert df is not None