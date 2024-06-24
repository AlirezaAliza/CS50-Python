import os
import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Invalid input - path")
        sys.exit(1)
    elif not fcheck(sys.argv[1]) and fcheck(sys.argv[2]):
        print("Invalid input")
        sys.exit(1)
    elif not fsame(sys.argv[1], sys.argv[2]):
        print("Input and output have different extensions")
        sys.exit(1)
    else:
        shirtwear(sys.argv[1], sys.argv[2])


def fcheck(input_filetype):
    valid = ["jpg", "jpeg", "png"]
    _, cf = input_filetype.split(".", maxsplit=1)
    if cf in valid:
        return True
    else:
        return False


def fsame(input_file, output_file):
    _, cf = input_file.split(".", maxsplit=1)
    if output_file.endswith(cf):
        return True
    else:
        return False


def shirtwear(input_file, output_file):
    shirt = Image.open("shirt.png")
    userimage = Image.open(input_file)

    a, b = shirt.size
    userimage = ImageOps.fit(userimage, (a, b))

    userimage.paste(shirt, shirt)
    userimage.save(output_file)


if __name__ == "__main__":
    main()
