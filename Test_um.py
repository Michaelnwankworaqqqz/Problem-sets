from um import count
import pytest


def test_recognizes_pattern():
    assert count("-- um ") == 1
    assert count("__um__") == 0
    assert count("um, so yummy") == 1
    assert count("Hello um there, my name is um Mike") == 2


def test_case_insensitivity():
    assert count("My name um is UM Michael") == 2
    assert count("WE'RE UM THE WORLD") == 1
