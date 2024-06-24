import sys
import inflect

p = inflect.engine()
from datetime import date, datetime


def main():
    a = input("Date of Birth:")
    validDate = date_validate(a)
    difdays = difcal(validDate)
    output = textout(difdays)
    print(output)


def date_validate(birthdate):
    try:
        input = date.fromisoformat(birthdate)
        return input
    except ValueError:
        sys.exit("Invalid date")


def textout(text):
    text = p.number_to_words(text, andword="")
    return text.capitalize() + " minutes"


def difcal(days):
    today = date.today()
    daysDiff = today - days
    daysDiff.days * 24 * 60
    return daysDiff.days * 24 * 60


if __name__ == "__main__":
    main()
