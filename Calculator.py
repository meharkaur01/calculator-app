x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=input("Options: Add, Subtract, Multiply, Divide\nWhat do you want to do:").lower()
if z=="add":
    print("Result",x+y)
elif z=="subtract":
    print("Result:",x-y)
elif z == "multiply":
    print("Result:", x * y)
elif z == "divide":
    if y != 0:
        print("Result:", x / y)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation. Please type Add, Subtract, Multiply, or Divide.")