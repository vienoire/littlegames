import math

print(''' ________________________________________________
|                                                |
|   _________________________________________    |
|  |   Welcome To The Sci-Calculator         |   |
|  |_________________________________________|   |
|         _____ _____ _____      _____           |
|        |  7  |  8  |  9  |    |  +  |          |
|        |_____|_____|_____|    |_____|          |
|        |  4  |  5  |  6  |    |  -  |          |
|        |_____|_____|_____|    |_____|          |
|        |  1  |  2  |  3  |    |  x  |          |
|        |_____|_____|_____|    |_____|          |
|        |  .  |  0  |  =  |    |  /  |          |
|        |_____|_____|_____|    |_____|          |
|________________________________________________|''')



while True:
    opr = input("Please Choose your Operation: *, /, +, -, log, sin, tan, cos, cot, ^, % --> ")
    if opr == "*":
        print("You chose multiplication. Enter the numbers you want to multiply.")
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Please only enter numbers")
            continue
        answer = num1 * num2
        shw = f"{num1} * {num2} = "
    elif opr == "/":
        print("You chose division. Enter the numbers you want to divide.")
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Please only enter numbers")
            continue
        answer = num1 / num2
        shw = f"{num1} / {num2} = "
    elif opr == "+":
        print("You chose addition. Enter the numbers you want to add.")
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Please only enter numbers")
            continue
        answer = num1 + num2
        shw = f"{num1} + {num2} = "
    elif opr == "-":
        print("You chose subtraction. Enter the numbers you want to subtract.")
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Please only enter numbers")
            continue
        answer = num1 - num2
        shw = f"{num1} - {num2} = "
    elif opr == "^":
        print("You chose exponentiation. Enter the base first, and then the exponent.")
        try:
            num1 = float(input("Base: "))
            num2 = float(input("Exponent: "))
        except ValueError:
            print("Please only enter numbers")
            continue
        answer = num1 ** num2
        shw = f"{num1}^{num2} = "
    elif opr == "%":
        print("You chose Modulo. Enter the base and the dividend to get the divisor.")
        try:
            num1 = float(input("Dividend: "))
            num2 = float(input("Divisor: "))
        except ValueError:
            print("Please only enter numbers")
            continue
        answer = num1 % num2
        shw = f"{num1} % {num2} = "
    elif opr == "log":
        print("You chose the logarithmic operation. Choose the base first and then the argument.")
        try:
            num1 = abs(float(input("Base: ")))
            num2 = abs(float(input("Argument: ")))
        except ValueError:
            print("Please only enter numbers")
            continue
        if num2 == 0:
            num2 = 0.1
        if num1 == 0 or num1 == 1:
            num1 += 0.1
        answer = math.log(num2) / math.log(num1)
        shw = f"log{num1}({num2}) = "
    elif opr == "sin":
        choice = input("You chose sine function. Do you want to calculate in radians or degrees? (enter pi or C)  ").lower()
        if choice == "pi":
            try:
                num1 = float(input("Enter only number x for x * pi--> "))
            except ValueError:
                print("Please only enter numbers")
                continue
            answer = math.sin(math.pi*num1)
            shw = f"sin({num1}pi) = "
        else:
            try:
                num1 = float(input("Enter the degree as a number: "))
            except ValueError:
                print("Please only enter numbers")
                continue
            rad = math.radians(num1)
            answer = math.sin(rad)
            shw = f"sin({num1}) = "
    elif opr == "cos":
        choice = input("You chose cosine function. Do you want to calculate in radians or degrees? (enter pi or C)  ").lower()
        if choice == "pi":
            try:
                num1 = float(input("Enter only number x for x * pi--> "))
            except ValueError:
                print("Please only enter numbers")
                continue
            answer = math.cos(math.pi*num1)
            shw = f"cos({num1}pi) = "
        else:
            try:
                num1 = float(input("Enter the degree as a number: "))
            except ValueError:
                print("Please only enter numbers")
                continue
            rad = math.radians(num1)
            answer = math.cos(rad)
            shw = f"cos({num1}) = "
    elif opr == "tan":
        choice = input("You chose tangent function. Do you want to calculate in radians or degrees? (enter pi or C)  ").lower()
        if choice == "pi":
            try:
                num1 = float(input("Enter only number x for x * pi--> "))
            except ValueError:
                print("Please only enter numbers")
                continue
            if num1 == int(num1):
                answer = float(0)
            elif (num1-0.5) == int(num1-0.5):
                num1 += 0.1
                answer = math.tan(math.pi * num1)
            else:
                answer = math.tan(math.pi*num1)
            shw = f"tan({num1}pi) = "
        else:
            try:
                num1 = float(input("Enter the degree as a number: "))
            except ValueError:
                print("Please only enter numbers")
                continue
            rad = math.radians(num1)
            if num1 % 180 == 0:
                answer = float(0)
            elif (num1-90) % 180 == 0:
                num1 += 0.1
                rad = math.radians(num1)
                answer = math.tan(rad)
            else:
                answer = math.tan(rad)
            shw = f"tan({num1}) = "
    elif opr == "cot":
        choice = input("You chose cotangent function. Do you want to calculate in radians or degrees? (enter pi or C)  ").lower()
        if choice == "pi":
            try:
                num1 = float(input("Enter only number x for x * pi--> "))
            except ValueError:
                print("Please only enter numbers")
                continue
            if num1 == int(num1):
                num1 += 0.1
                answer = 1 / math.tan(math.pi * num1)
            elif (num1-0.5) == int(num1-0.5):
                answer = float(0)
            else:
                answer = 1 / math.tan(math.pi * num1)
            shw = f"cot({num1}pi) = "
        else:
            try:
                num1 = float(input("Enter the degree as a number: "))
            except ValueError:
                print("Please only enter numbers")
                continue
            rad = math.radians(num1)
            if num1 % 180 == 0:
                num1 += 0.1
                rad = math.radians(num1)
                answer = 1 / math.tan(rad)
            elif (num1-90) % 180 == 0:
                answer = float(0)
            else:
                answer = 1 / math.tan(rad)
            shw = f"cot({num1}) = "
    else:
        shw = "Please choose a proper operator"
        answer = "\n\t\t\tNext time"

    print(f''' ________________________________________________
    |                                                |
    |   _________________________________________    |
          {shw}{answer}
    |  |_________________________________________|   |
    |         _____ _____ _____      _____           |
    |        |  7  |  8  |  9  |    |  +  |          |
    |        |_____|_____|_____|    |_____|          |
    |        |  4  |  5  |  6  |    |  -  |          |
    |        |_____|_____|_____|    |_____|          |
    |        |  1  |  2  |  3  |    |  x  |          |
    |        |_____|_____|_____|    |_____|          |
    |        |  .  |  0  |  =  |    |  /  |          |
    |        |_____|_____|_____|    |_____|          |
    |________________________________________________|''')

    again = input("Do you want to restart? yes or no  ").lower()
    if again != "yes":
        break

