import time
import math


print("\n to the  calc\n")

while True:
    def _input():
        global x
        global y
        x = float(input("Enter the 1st number: "))
        y = float(input("Enter the 2nd number: "))
        return x, y

    time.sleep(4.0)
    operations = ["Addition", "Subtraction", "Multiplication", "Divion",
                "Square", "Square root", "Factorial", "Angle conversion", "Exit"]

    for idx, operation in enumerate(operations, start=1):
        print(f"{idx}. {operation}")

    calc = int(input("Choose the operation >>> "))

    if calc == 1:
        _input()
        print(f"{x} + {y}  = {x + y}")
    elif calc == 2:
        _input()
        print(f"{x} - {y}  = {x - y}")
    elif calc == 3:
        _input()
        print(f"{x} * {y}  = {x * y}")
    elif calc == 4:
        _input()
        print(f"{x} / {y}  = {x / y}")
    elif calc == 5:
        x = int(input("Enter the number: "))
        print(f"{x}^2 = {x ** 2}")
    elif calc == 6:
        x = int(input("Enter the number: "))
        print(f"square root of {x} = {x ** 0.5}")
    elif calc == 7:
         x = int(input("Enter the number: "))
         print(f"{x}! = {math.factorial(x)}")
    elif calc == 8:
        angle = input("\n1. rad to degree\n2.degree to rad\nPress[1/2]>>> ")

        if angle == "1":
            x = float(input("Radian: "))
            print(f"{x} rad = {math.degrees(x)} degree")
        else:
            x = float(input("Degree: "))
            print(f"{x} degree = {math.radians(x)} rad")
    elif calc == 9:
        break
    else:
        print("Invalid choice")
