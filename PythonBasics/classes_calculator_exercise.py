"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to take two numbers and add them and return the sum
* method to take two numbers and subtract the second number from the first number and return the diff
* method to take two numbers and return the multiplication of the two
* method to divide two numbers and return the result (first number divided by second number)

"""


class BasicCalculator:
    def __init__(self):
        print("Basic Calculator launched...")

    @staticmethod  # decorator
    def add(x, y):
        return x + y

    @staticmethod  # decorator
    def subtract(x, y):
        return x - y

    @staticmethod  # decorator
    def multiply(x, y):
        return x * y

    @staticmethod  # decorator
    def divide(x, y):
        return x / y


calculator = BasicCalculator()

a = int(input("First number: "))
b = int(input("Second number: "))

print(f"The Addition of {a} and {b} is equal to: {calculator.add(a, b)}")
print(f"The Subtraction of {a} and {b} is equal to: {calculator.subtract(a, b)}")
print(f"The Multiplication of {a} and {b} is equal to: {calculator.multiply(a, b)}")
print(f"The Division of {a} and {b} is equal to: {calculator.divide(a, b)}")
