from working import convert
import pytest

def test_off_by_one_error():
    assert convert("4:30 PM to 5:30 PM") == "16:30 to 17:30"
    assert convert("7 AM to 8:00 AM") == "07:00 to 08:00"

def test_minutes_by_five():
    assert convert("6:00 AM to 6:05 AM") == "06:00 to 06:05"


def test_out_range_times():
    with pytest.raises(ValueError):
        convert("9:60 PM to 4:60 AM")
    with pytest.raises(ValueError):
        convert("30:04 PM to 25:00 AM")

def test_time_format():
    with pytest.raises(ValueError):
        convert("9 AM 5:0 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 13:00 PM")

def test_convert_return_value():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("4:00 AM to 10 PM") == "04:00 to 22:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
