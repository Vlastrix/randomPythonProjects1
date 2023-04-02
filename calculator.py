logo = logo = """
 _____________________
|  _________________  |
| | Vlastrix  12+1. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

#calculator

def add(n1, n2):
  """Adds the two numbers together."""
  return n1 + n2

def subtract(n1, n2):
  """Subtracts the two numbers given."""
  return n1 - n2

def multiply(n1, n2):
  """Multiplies the two numbers."""
  return n1 * n2

def divide(n1,n2):
  """Divides the two numbers given."""
  return n1 / n2


operations = {
  "+": add, 
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calc():
    first_num = float(input("What is the first number?: "))
    for keys in operations:
        print(keys)

    should_continue = True
    while should_continue is True:
        operation_symbol = input("Pick an operation : ")
        second_num = float(input("What's the next number?: "))

        calculation_fuction = operations[operation_symbol]
        answer = calculation_fuction(first_num, second_num)

        print(f"{first_num} {operation_symbol} {second_num} = {answer}")

        progress = input(f"Type 'c' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'e' to exit: ")
        
        if progress == "c":
            first_num = answer
        elif progress == "n":
            calc()
        elif progress == "e":
            exit()

calc() 
