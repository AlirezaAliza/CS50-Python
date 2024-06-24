def main():
    list_to_do_list = ["+","-","*","/"]


    print("----------------------------------")
    number_1 = int(input("|Please enter your number :"))

    print("----------------------------------")
    op = input("|Please enter your op: ")

    print("----------------------------------")
    number_2 = int(input("|Please enter your number: "))
    return list_to_do_list,number_1,op,number_2

list_to_do_list, number_1, op, number_2 = main()


def check_for_number_1(number_1):
    if number_1 != "":
        pass
    else:
        print("Error")

def check_for_op(list_to_do_list, op):
    if op != "" and op in list_to_do_list:
        if op == "+":
            print("----------------------------------")
            c = number_1 + number_2
            print(f"|              {c}               |")
            print("----------------------------------")

        if op == "-":
            print("----------------------------------")
            c = number_1 - number_2
            print(f"|              {c}               |")
            print("----------------------------------")

        if op == "*":
            print("----------------------------------")
            c = number_1 * number_2
            print(f"|              {c}               |")
            print("----------------------------------")

        if op == "/":
            print("----------------------------------")
            c = number_1 / number_2
            print(f"|              {c}               |")
            print("----------------------------------")

    else:
        print("Error")

def check_for_number_2(number_2):
    if number_2 != "":
        pass
    else:
        print("Error")

check_for_op(list_to_do_list, op)
check_for_number_1(number_1)
check_for_number_2(number_2)

if __name__ == "__main__":
    main()

