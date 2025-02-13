from bank import value

import pytest


def test_greetings():
    assert value("Hello") == 0
    assert value("Hello, Dave") == 0
    assert value("How's it going?") == 20
    assert value("How're you doing?") == 20
    assert value("What's happening?") == 100


def test_case_insensitivity():
    assert value("HEY") == 20
    assert value("hey") == 20
    assert value("WHAT'S UP?") == 100
    assert value("what's up?") == 100


def test_correct_values():
    assert value("What's good?") == 100
    assert value("How're you?") == 20
    assert value("Hello sir") == 0
