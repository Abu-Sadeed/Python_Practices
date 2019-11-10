num1 = input("Enter First Number: ")
op = input("Enter Operation: ")
num2 = input("Enter Second Number: ")

def calculate(first, op, second):
    try:
        if op == "+":
            add = float(num1) + float(num2)
            print(add)
        elif op == "-":
            sub = float(num1) - float(num2)
            print(sub)
        elif op == "*":
            mul = float(num1) * float(num2)
            print(mul)
        elif op == "/":
            div = float(num1) / float(num2)
            print(div)
        elif op == "%":
            mod = float(num1) % float(num2)
            print(mod)
        else:
            print("Invalid")
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print(err)
    

calculate(num1, op, num2)