from datetime import date, datetime


def get_age(birthdate_str: str) -> int:
    """Return age in years given birthdate in YYYY-MM-DD format."""
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


if __name__ == "__main__":
    bd = input("Enter birthdate (YYYY-MM-DD): ")
    print(get_age(bd))
