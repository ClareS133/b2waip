print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid choice")

# This is a simple calculator that performs basic arithmetic operations based on user input.
# The user is prompted to enter two numbers and choose an operation (addition, subtraction, multiplication, or division).
# The program then checks the user's choice and performs the corresponding operation on the two numbers.
# If the user chooses division and the second number is zero, the program displays an error message to prevent division by zero.
# The program uses conditional statements to determine which operation to perform based on the user's choice. It also includes error handling for division by zero to ensure that the program does not crash and provides a user-friendly message instead.
# The program is designed to be simple and easy to use, allowing users to perform basic calculations without needing to understand complex programming concepts. It demonstrates the use of input, output, conditional statements, and error handling in Python.
# The user is prompted to enter two numbers and choose an operation (addition, subtraction, multiplication, or division). The program then performs the chosen operation and displays the result. If the user chooses division and the second number is zero, an error message is displayed to prevent division by zero.
# The number inputs are converted to floats to allow for decimal calculations. The program uses a series of if-elif statements to determine which operation to perform based on the user's choice. If the user enters an invalid choice, an error message is displayed. The program also includes error handling for division by zero, ensuring that the user is informed of the error without crashing the program.
# The program then performs the chosen operation and displays the result. If the user chooses division and the second number is zero, an error message is displayed to prevent division by zero.
# The program demonstrates User input, Type conversion (float), Conditionals (if, elif, else), Basic arithmetic operatrions, Error handling (division by zero).



