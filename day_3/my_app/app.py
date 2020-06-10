from helpers import calculator
# import helpers.calculator
# from helpers.calculator import add

def add_numbers(num1, num2):
    return calculator.add(num1, num2)

def subtract_numbers(num1, num2):
    return calculator.subtract(num1, num2)

print(add_numbers(4, 5))
