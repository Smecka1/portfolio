import os

def clear_screen():
    # Clear the terminal screen depending on the operating system.
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')

def do_operation(a, operation, b):
    # Perform the specified operation on two numbers.
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b

def get_number():
    # Continuously prompt the user for a valid number until they provide one.
    while True:
        try:
            return float(input("Zadej číslo: "))
        except ValueError:
            print("Musíš zadat ČÍSLO!")

def get_operator():
    # Continuously prompt the user for a valid operator until they provide one.
    valid_operator = ["+", "-", "*", "/"]
    while True:
        operator = input("+  -  *  / : ")
        if operator in valid_operator:
            return operator
        else:
            print(f"{operator} - není validní operátor")

def continue_or_end():
    # Prompt the user to choose the next action: continue with result, start new calculation, or end.
    valid = ["1", "2", "3"]
    while True:
        choice = input("Vyber: 1) Pokračovat s výsledkem, 2) Nové zadání, 3) Konec: ")
        if choice in valid:
            return choice
        else:
            print("Můžeš volit pouze: 1, 2, 3")

########################################################################################################################

run = "run"  # Initialize the program state.
result = 0  # Variable to store the current result.

while run != "3":  # Continue the program until the user chooses to end.
    clear_screen()
    if run == "1":
        # If the user wants to continue with the previous result.
        print(f"Výsledek:    {result}")
        number_a = result
    else:
        # Prompt the user for the first number.
        number_a = get_number()

    # Get the operator from the user.
    operator = get_operator()

    # Prompt the user for the second number.
    number_b = get_number()

    if operator == "/" and number_b == 0:
        # Handle division by zero.
        print("Nulou nelze dělit.")
    else:
        # Perform the calculation and display the result.
        result = do_operation(number_a, operator, number_b)
        print(f"{22 * '*'}\n{number_a} {operator} {number_b} = {result}\n")

    # Ask the user what to do next.
    run = continue_or_end()
