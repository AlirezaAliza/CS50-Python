def main():
    User = input("Input: ").strip()
    print(f"Output: {shorten(word=User)}")


def shorten(word):
    Vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for Letter in word.lower():
        if Letter in Vowels:
            word = word.replace(Letter, "")

    return word

if __name__ == "__main__":
    main()

