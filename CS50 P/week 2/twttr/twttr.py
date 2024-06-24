def main():
    User = input("Input: ").strip()

    print(f"Output: {shorten(word=User)}")


def shorten(word):

    for i in ['a','o','u','e','i','A','O','U','E','I']:
        word = word.replace(i,"")

    return word


if __name__ == "__main__":
    main()

