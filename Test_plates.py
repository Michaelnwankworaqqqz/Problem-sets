from plates import is_valid

import pytest


def test_return_value():
    assert is_valid("GOODBYE") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("50") == False


def test_plate_lenght():
    with pytest.raises(AssertionError):
        assert is_valid("BOO34YI")
        assert is_valid("w")


def test_num_placement():
        assert is_valid("ver01") == False
        assert is_valid("w0men") == False


def test_punctuation():
    with pytest.raises(AssertionError):
        assert is_valid("D'KING")


def test_alphabetical_beginning():
    with pytest.raises(AssertionError):
        assert is_valid("0well")


def test_alphanumberic_char():
    with pytest.raises(AssertionError):
        assert is_valid("CS/50")
