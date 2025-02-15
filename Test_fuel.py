from fuel import convert, gauge

import pytest


def test_input_format():
    with pytest.raises(ValueError):
        assert convert("cat/dog")

def test_numerator_denominator():
    with pytest.raises(ValueError):
        assert convert("4/1")

def test_correct_denominator():
    with pytest.raises(ZeroDivisionError):
        assert convert("2/0")

def test_incorrect_returns():
    assert convert("1/2") == 50


def test_conditions():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(49) == "49%"

def test_adequate_response():
    with pytest.raises(TypeError):
        assert gauge("14")
