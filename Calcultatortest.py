# Basic Calculator Program

# Define the function for addition
def add(num1, num2):
    return num1 + num2

# Define the function for subtraction
def subtract(num1, num2):
    return num1 - num2

# Define the function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Define the function for division
def divide(num1, num2):
    return num1 / num2

# Ask the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the requested operation
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    print("Invalid operation selected.")
    exit()

# Print the result
print("Result:", result)