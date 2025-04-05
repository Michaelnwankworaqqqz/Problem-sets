from datetime import datetime, date
from seasons import age_in_minutes_calc
import pytest


def test_age_input():
    assert age_in_minutes_calc(datetime.strptime("2024-04-04", "%Y-%m-%d")) == 525600
    assert age_in_minutes_calc(datetime.strptime("2023-04-04", "%Y-%m-%d")) == 1052640
    assert age_in_minutes_calc(datetime.strptime("1999-04-29", "%Y-%m-%d")) == 13639680


def test_valueerror_check():
    with pytest.raises(ValueError):
        age_in_minutes_calc(datetime.strptime("29-january-2012", "%Y-%m-%d"))

