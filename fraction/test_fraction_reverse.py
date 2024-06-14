import pytest
from fraction import Fraction

def test_fraction_radd_method():
    # Test case 1: Adding two fractions with positive values
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(3, 4)
    result = fraction2 + fraction1
    assert result.numerator == 5
    assert result.denominator == 4

    # Test case 2: Adding two fractions with negative values
    fraction3 = Fraction(-1, 3)
    fraction4 = Fraction(-2, 5)
    result = fraction4 + fraction3
    assert result.numerator == -11
    assert result.denominator == 15

    # Test case 3: Adding a fraction with zero
    fraction5 = Fraction(1, 2)
    zero_fraction = Fraction(0, 1)
    result = fraction5 + zero_fraction
    assert result.numerator == 1
    assert result.denominator == 2

    # Test case 4: Adding fractions where one is zero
    fraction6 = Fraction(3, 5)
    result = fraction6 + zero_fraction
    assert result.numerator == 3
    assert result.denominator == 5

    # Test case 5: Adding fractions with different denominators
    fraction7 = Fraction(1, 3)
    fraction8 = Fraction(2, 5)
    result = fraction8 + fraction7
    assert result.numerator == 11
    assert result.denominator == 15

    # Test case 6: Adding fractions with large numerators and denominators
    fraction9 = Fraction(987654321, 123456789)
    fraction10 = Fraction(987, 654)
    result = fraction10 + fraction9
    assert result.numerator == 28436213951
    assert result.denominator == 2990397778
    
    
def test_fraction_radd_method_int():
    # Test case 1: Adding an integer to a fraction with positive values
    fraction1 = Fraction(1, 2)
    result = 2 + fraction1
    assert result.numerator == 5
    assert result.denominator == 2

    # Test case 2: Adding an integer to a fraction with negative values
    fraction2 = Fraction(-2, 3)
    result = -3 + fraction2
    assert result.numerator == -11
    assert result.denominator == 3

    # Test case 3: Adding zero to a fraction
    fraction3 = Fraction(3, 4)
    result = 0 + fraction3
    assert result.numerator == 3
    assert result.denominator == 4

    # Test case 4: Adding a negative integer to a fraction
    fraction4 = Fraction(5, 6)
    result = -4 + fraction4
    assert result.numerator == -19
    assert result.denominator == 6

    # Test case 5: Adding an integer to a fraction with different denominator
    fraction5 = Fraction(1, 5)
    result = 7 + fraction5
    assert result.numerator == 36
    assert result.denominator == 5

    # Test case 6: Adding an integer to a fraction with large numerators and denominators
    fraction6 = Fraction(987654321, 123456789)
    result = 1000000 + fraction6
    assert result.numerator == 13717530739369
    assert result.denominator == 13717421
    
    
    # Test case 6: Adding a positive integer to a fraction resulting in zero
    fraction7 = Fraction(21, 3)
    result = -7 + fraction7
    assert result.numerator == 0
    assert result.denominator == 1


    # Test case 6: Adding a negative integer to a fraction resulting in zero
    fraction8 = Fraction(21, -3)
    result = 7 + fraction8
    assert result.numerator == 0
    assert result.denominator == 1
