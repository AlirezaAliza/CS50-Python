import sys
from random import choice
from pyfiglet import Figlet


f = Figlet()
fontlist = f.getFonts()


if len(sys.argv) == 1 :
    a = input("Input: ").strip()
    f.setFont(font = choice(fontlist))
    print(f.renderText(a))

elif len(sys.argv) == 3 :
    if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in fontlist:
        a = input("Input: ").strip()
        f.setFont(font = str(sys.argv[2]))
        print(f.renderText(a))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
