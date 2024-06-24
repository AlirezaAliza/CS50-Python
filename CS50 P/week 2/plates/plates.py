symbols = [" ", ".", "?", "!", ",", ":", ";", "(", ")", "[", "]", "'", "-", '"', "/", "\\", "`", "@", "#", "*", ]
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validated = ""
    numbcheck = 0

    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:
                if ch not in symbols:
                    if ch.isnumeric() and numbcheck ==0 and ch != "":
                        numbcheck += 1
                        validated += ch
                    elif ch .isnumeric() and numbcheck > 0:
                        numbcheck += 1
                        validated += ch
                    elif ch.isalpha() and numbcheck == 0:
                        validated += ch

    if validated == s :
        return True
    else:
        return False

main()
