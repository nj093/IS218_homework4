from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:

    def add(a,b):
        calculation = Calculation(a, b, add)
        return calculation.get_result()

    def subtract(a,b):
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()
    
    def multiply(a,b):
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()
    
    def divide(a,b):
        calculation = Calculation(a, b, divide)
        return calculation.get_result()