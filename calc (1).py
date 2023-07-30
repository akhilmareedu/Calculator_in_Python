from sympy import *

def calculator():
    while True:
        print("\nSimple Calculator")
        print("Enter 'quit' to exit\n")
        user_input = input("Enter an expression: ")

        if user_input == 'quit':
            break

        try:
            expr = sympify(user_input)
            print(f"The result is: {expr.evalf()}")
        except SympifyError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()
