x, y, z = input("enter an expression:").strip().split(" ")
if y == "+":
    ans = float(x) + float(z)
elif y == "-":
    ans = float(x) - float(z)
elif y == "*":
    ans = float(x) * float(z)
elif y == "/":
    ans = float(x) / float(z)

print(f"{ans:.1f}")
