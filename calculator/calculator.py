import art

def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2

print(art.logo)
last_number = 0

while True:
    if last_number > 0:
        number1 = last_number
    else:
        number1 = float(input("What's the first number?: "))
    print("+\n"+"-\n"+"*\n"+"/\n")
    operation = input("Pick an operation: ")
    number2 = float(input("What's the second number?: "))
    keys = {"+": add(number1, number2),
            "-": subtract(number1, number2),
            "*": multiply(number1,number2),
            "/": divide(number1,number2)}
    result = keys[operation]

    print(f"{number1} {operation} {number2} = {result}")

    user_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower().strip()
    if user_continue == "y":
        last_number = result
    else:
        print("\n" * 20)
        last_number = 0
        break










