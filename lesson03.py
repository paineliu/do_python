from calendar import c


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = input("Enter +-/*: ")

if c == "+":
    result = (a) + (b)
elif c == "-":
  result = (a) - (b)
elif c == "*":
    result = (a) * (b)
elif c == "/":
    result = (a) / (b)
else:
    print("Invalid operator")
    result = 0

print("The result is ", result, ".")