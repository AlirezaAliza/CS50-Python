import sys
import requests

apilink = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    print(f"${coindesk(testinput()):,.4f}")


def testinput():
    try:
        if len(sys.argv) < 2:
            print("Missing command-line argument")
            sys.exit(1)
        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")
            sys.exit(1)
        else:
            return float(sys.argv[1])
    except (TypeError, ValueError):
        print("Command-line argument is not a number")
        sys.exit(1)


def coindesk(uinput):
    try:
        response = requests.get(apilink)
        a = response.json()
        b = a["bpi"]["USD"]["rate_float"]
        c = uinput * b
    except requests.RequestException:
        print("CONNECTION ERROR!")
        sys.exit()
    return c


if __name__ == "__main__":
    main()
