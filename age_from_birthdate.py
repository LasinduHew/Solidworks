from datetime import date, datetime


def calculate_age(birthdate: date | str) -> int:
    """Return age in years for the given birthdate.

    Args:
        birthdate: Either a ``datetime.date`` instance or a string in
            ``YYYY-MM-DD`` format representing the birth date.

    Returns:
        Age in complete years as of today's date.
    """
    if isinstance(birthdate, str):
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()

    today = date.today()
    years = today.year - birthdate.year
    has_had_birthday = (today.month, today.day) >= (birthdate.month, birthdate.day)
    if not has_had_birthday:
        years -= 1
    return years


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python age_from_birthdate.py YYYY-MM-DD")
        raise SystemExit(1)

    print(calculate_age(sys.argv[1]))
