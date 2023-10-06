# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    # Prompt the user for input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Take input for the operation
    operation = input("Enter operation (1/2/3/4/5): ")

    if operation == '5':
        print("Exiting the calculator. Goodbye!")
        break

    # Perform the calculation based on the selected operation
    if operation == '1':
        print("Result:", add(num1, num2))
    elif operation == '2':
        print("Result:", subtract(num1, num2))
    elif operation == '3':
        print("Result:", multiply(num1, num2))
    elif operation == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")

