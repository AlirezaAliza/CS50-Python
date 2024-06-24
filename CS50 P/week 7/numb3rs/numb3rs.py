import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        a = ip.split(".", maxsplit=3)
        for r in a:
            if int(r) > 255 or len(a) < 4:
                return False
    except ValueError:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
