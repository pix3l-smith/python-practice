import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error: cannot divide by zero"
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = float(input("Enter a number: "))
continue_calculations = True

print("Welcome to the calculator!")
while continue_calculations == True:
    operator = input("Enter an operator:\n(+ for addition, - for subtraction, * for multiplication, / for division):\n")

    if operator in operations:
        num2 = float(input("Enter another number: "))
        result = operations[operator](num1, num2)
        print(f"\nRESULT:\n{num1:g} {operator} {num2:g} = {result:g}\n\n----------")
        continue_question = input(f"Type 'y' to continue calculating from {result:g}\nType 'n' to start a new calculation:\nType 'q' to quit\n").lower()

        if continue_question == "y":
            num1 = result

        elif continue_question == "n":
            clear_screen()
            num1 = float(input("Enter a number: "))

        else:
            continue_calculations = False
            clear_screen()
            print("Goodbye!")

    else:
        print("invalid operator")
