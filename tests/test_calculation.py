from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('25'), Decimal('15'), add, Decimal('40')), 
    (Decimal('50'), Decimal('10'), subtract, Decimal('40')),
    (Decimal('5'), Decimal('5'), multiply, Decimal('25')), 
    (Decimal('50'), Decimal('5'), divide, Decimal('10')),  
    (Decimal('32.5'), Decimal('30'), add, Decimal('62.5')),  
    (Decimal('30'), Decimal('22.5'), subtract, Decimal('7.5')), 
    (Decimal('5.5'), Decimal('10.5'), multiply, Decimal('57.75')),  
    (Decimal('100'), Decimal('20'), divide, Decimal('5')), 
])

def test_calculation_operations(a, b, operation, expected):

    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():

    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():

    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()