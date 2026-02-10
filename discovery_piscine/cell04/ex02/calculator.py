a = input("Give me the first number: ")
b = input("Give me the second number: ")

x = int(a)
y = int(b)

print("Thank you!")
print(f"{int(x) if x.is_integer() else x} + {int(y) if y.is_integer() else y} = {x + y}")
print(f"{int(x) if x.is_integer() else x} - {int(y) if y.is_integer() else y} = {x - y}")
print(f"{int(x) if x.is_integer() else x} / {int(y) if y.is_integer() else y} = {x / y}")
print(f"{int(x) if x.is_integer() else x} * {int(y) if y.is_integer() else y} = {x * y}")
