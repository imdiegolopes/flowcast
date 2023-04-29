from datetime import datetime
from src.domain.entity.mood import Mood
import pytest

def test_valid_mood():
    id = "1"
    date = datetime.now().strftime("%Y-%m-%d")
    feeling = "happy"
    intensity = 5
    comments = "This is a test mood."
    activity = "testing"
    mood = Mood(id, date, feeling, intensity, comments, activity)
    assert mood.id == id
    assert mood.date == date
    assert mood.feeling == feeling
    assert mood.intensity == intensity
    assert mood.comments == comments
    assert mood.activity == activity

def test_missing_date():
    with pytest.raises(ValueError):
        Mood("1", None, "happy", 5, "This is a test mood.", "testing")

def test_missing_feeling():
    with pytest.raises(ValueError):
        Mood("1", datetime.now().strftime("%Y-%m-%d"), None, 5, "This is a test mood.", "testing")

def test_missing_intensity():
    with pytest.raises(ValueError):
        Mood("1", datetime.now().strftime("%Y-%m-%d"), "happy", None, "This is a test mood.", "testing")

def test_intensity_out_of_range():
    with pytest.raises(ValueError):
        Mood("1", datetime.now().strftime("%Y-%m-%d"), "happy", 20, "This is a test mood.", "testing")