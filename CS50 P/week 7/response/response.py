import validators

address = input("What's your email address? ").strip()

if validators.email(address):
    print("Valid")
else:
    print("Invalid")
