import pytest

from src.utils import greet


def test_greet_basic():
    assert greet("V") == "Hello, V!"


def test_greet_empty_raises():
    with pytest.raises(ValueError):
        greet("")
