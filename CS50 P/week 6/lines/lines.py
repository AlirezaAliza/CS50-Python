import sys
import os

def main():
    if len(sys.argv)<2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) >2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    elif not sys .argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    else:
        print(conter(sys.argv[1]))

def conter(Python_file):
    rline = 0
    with open(Python_file,"r") as lines:
        tlins = list(enumerate(lines.readlines(),start=1))
        for nline, lines in tlins:
            if (
                lines.strip().startswith("#")
                or lines.strip().startswith("\n")
                or lines.isspace()
            ):
                rline +=1
    return int(tlins[-1][0]) -rline

if __name__ == "__main__":
    main()
