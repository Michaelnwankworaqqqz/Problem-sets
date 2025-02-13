from twttr import shorten

import pytest

def test_upper_vowels():
    assert shorten("Twitter") == "Twttr"
    assert shorten("WHAT'S YOUR NAME?") == "WHT'S YR NM?"


def test_lower_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("what's your name?") == "wht's yr nm?"


def test_omit_nums():
    assert shorten("Rainbow001") == "Rnbw001"


def test_error():
    with pytest.raises(NameError):
        shorten(CS50)
