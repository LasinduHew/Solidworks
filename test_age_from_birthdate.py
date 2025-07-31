from datetime import date

from age_from_birthdate import calculate_age


def test_calculate_age():
    today = date.today()
    birthdate = date(today.year - 30, today.month, today.day)
    assert calculate_age(birthdate) == 30
