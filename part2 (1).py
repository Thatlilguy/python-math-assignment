# Part 2: Multiplication and Division

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculations
product = num1 * num2

# Check for division by zero
if num2 != 0:
    quotient = num1 / num2
    print("The product is:", product)
    print("The quotient is:", quotient)
else:
    print("The product is:", product)
    print("Cannot divide by zero.")