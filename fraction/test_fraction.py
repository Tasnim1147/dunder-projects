import pytest
import math
from fraction import Fraction

def test_fraction_initialization():
    """
    Test the initialization of the Fraction class.
    """

    # Test with positive numerator and denominator
    frac = Fraction(1, 2)
    assert frac.numerator == 1
    assert frac.denominator == 2

    # Test with negative numerator and positive denominator
    frac = Fraction(-3, 4)
    assert frac.numerator == -3
    assert frac.denominator == 4

    # Test with positive numerator and negative denominator
    frac = Fraction(5, -6)
    assert frac.numerator == 5
    assert frac.denominator == -6

    # Test with negative numerator and negative denominator
    frac = Fraction(-7, -8)
    assert frac.numerator == -7
    assert frac.denominator == -8

    # Test with zero numerator
    frac = Fraction(0, 9)
    assert frac.numerator == 0
    assert frac.denominator == 9

def test_fraction_initialization_zero_denominator():
    """
    Test that initializing a Fraction with a zero denominator raises a ValueError.
    """

    with pytest.raises(ValueError, match=r"Denominator cannot be zero"):
        Fraction(3, 0)
        
    with pytest.raises(ValueError, match=r"Denominator cannot be zero"):
        Fraction(5, 0)
        
        
def test_fraction_str_method():
    """
    Test the __str__ method of the Fraction class.
    """

    # Test with positive fraction
    frac = Fraction(1, 2)
    assert str(frac) == "1/2"

    # Test with negative fraction
    frac = Fraction(-3, 4)
    assert str(frac) == "-3/4"

    # Test with zero numerator
    frac = Fraction(0, 7)
    assert str(frac) == "0"

    # Test with denominator equal to 1 (integer representation)
    frac = Fraction(5, 1)
    assert str(frac) == "5"

    # Test with fraction where numerator and denominator are negative
    frac = Fraction(-5, -6, simplify=True)
    assert str(frac) == "5/6"  

    # Test with denominator equal to -1 (integer representation of negative fraction)
    frac = Fraction(-5, 1)
    assert str(frac) == "-5"
    
def test_fraction_add_method():
    """
    Test the __add__ method of the Fraction class.
    """

    # Test with positive fractions
    frac1 = Fraction(1, 4)
    frac2 = Fraction(1, 4)
    result = frac1 + frac2
    assert result.numerator == 1
    assert result.denominator == 2  # 1/4 + 1/4 = 2/4 = 1/2

    # Test with negative fractions
    frac1 = Fraction(-1, 4)
    frac2 = Fraction(-1, 4)
    result = frac1 + frac2
    assert result.numerator == -1
    assert result.denominator == 2  # -1/4 + -1/4 = -2/4 = -1/2

    # Test with positive and negative fractions
    frac1 = Fraction(1, 4)
    frac2 = Fraction(-1, 4)
    result = frac1 + frac2
    assert result.numerator == 0
    assert result.denominator == 1  # 1/4 + -1/4 = 0/4 = 0

    # Test with different denominators
    frac1 = Fraction(1, 2)
    frac2 = Fraction(1, 3)
    result = frac1 + frac2
    assert result.numerator == 5
    assert result.denominator == 6  # 1/2 + 1/3 = 3/6 + 2/6 = 5/6

    # Test with integer addition
    frac1 = Fraction(3, 4)
    result = frac1 + 2  # Adding integer to fraction
    assert result.numerator == 11
    assert result.denominator == 4  # 3/4 + 2 = 3/4 + 8/4 = 11/4

    # Test with zero numerator
    frac1 = Fraction(0, 4)
    frac2 = Fraction(1, 4)
    result = frac1 + frac2
    assert result.numerator == 1
    assert result.denominator == 4  # 0/4 + 1/4 = 1/4

    # Test with zero fractions
    frac1 = Fraction(0, 4)
    frac2 = Fraction(0, 4)
    result = frac1 + frac2
    assert result.numerator == 0
    assert result.denominator == 1  # 0/4 + 0/4 = 0/1 = 0

    # Test with negative fraction and integer
    frac1 = Fraction(-1, 4)
    result = frac1 + 2  # Adding integer to negative fraction
    assert result.numerator == 7
    assert result.denominator == 4  # -1/4 + 8/4 = 7/4

    # Test with negative integer and fraction
    frac1 = Fraction(1, 4)
    result = frac1 + (-2)  # Adding negative integer to fraction
    assert result.numerator == -7
    assert result.denominator == 4  # -2 + 1/4 = -8/4 + 1/4 = -7/4

    # Test with large integers
    frac1 = Fraction(999999999, 1000000000)
    frac2 = Fraction(1, 1000000000)
    result = frac1 + frac2
    assert result.numerator == 1
    assert result.denominator == 1  # 999999999/1000000000 + 1/1000000000 = 1000000000/1000000000 = 1
    
def test_fraction_add_method_unsupported_types():
    """
    Test that adding a non-Fraction/non-int type raises a TypeError with exact message.
    """
    frac = Fraction(1, 2)
    
    with pytest.raises(TypeError, match=r"Unsupported operand types for \+: 'Fraction' and 'str'"):
        frac + "test"
        
    with pytest.raises(TypeError, match=r"Unsupported operand types for \+: 'Fraction' and 'float'"):
        frac + 1.0
        
def test_fraction_sub_method():
    """
    Test the __sub__ method of the Fraction class.
    """

    # Test with positive fractions
    frac1 = Fraction(3, 4)
    frac2 = Fraction(1, 4)
    result = frac1 - frac2
    assert result.numerator == 1
    assert result.denominator == 2  # 3/4 - 1/4 = 2/4 = 1/2

    # Test with negative fractions
    frac1 = Fraction(-3, 4)
    frac2 = Fraction(-1, 4)
    result = frac1 - frac2
    assert result.numerator == -1
    assert result.denominator == 2  # -3/4 - (-1/4) = -2/4 = -1/2

    # Test with positive and negative fractions
    frac1 = Fraction(1, 4)
    frac2 = Fraction(-1, 4)
    result = frac1 - frac2
    assert result.numerator == 1
    assert result.denominator == 2  # 1/4 - (-1/4) = 2/4 = 1/2

    # Test with different denominators
    frac1 = Fraction(1, 2)
    frac2 = Fraction(1, 3)
    result = frac1 - frac2
    assert result.numerator == 1
    assert result.denominator == 6  # 1/2 - 1/3 = 3/6 - 2/6 = 1/6

    # Test with integer subtraction
    frac1 = Fraction(3, 4)
    result = frac1 - 1  # Subtracting integer from fraction
    assert result.numerator == -1
    assert result.denominator == 4  # 3/4 - 1 = 3/4 - 4/4 = -1/4

    # Test with zero numerator
    frac1 = Fraction(0, 4)
    frac2 = Fraction(1, 4)
    result = frac1 - frac2
    assert result.numerator == -1
    assert result.denominator == 4  # 0/4 - 1/4 = -1/4

    # Test with zero fractions
    frac1 = Fraction(0, 4)
    frac2 = Fraction(0, 4)
    result = frac1 - frac2
    assert result.numerator == 0
    assert result.denominator == 1  # 0/4 - 0/4 = 0/4 = 0

    # Test with negative fraction and integer
    frac1 = Fraction(-1, 4)
    result = frac1 - 1  # Subtracting integer from negative fraction
    assert result.numerator == -5
    assert result.denominator == 4  # -1/4 - 1 = -1/4 - 4/4 = -5/4

    # Test with large integers
    frac1 = Fraction(1000000000, 1000000001)
    frac2 = Fraction(1, 1000000001)
    result = frac1 - frac2
    assert result.numerator == 999999999
    assert result.denominator == 1000000001  
    
def test_fraction_mul_method():
    """
    Test the __mul__ method of the Fraction class.
    """

    # Test with positive fractions
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)
    result = frac1 * frac2
    assert result.numerator == 1
    assert result.denominator == 3  # 1/2 * 2/3 = 2/6 = 1/3

    # Test with negative fractions
    frac1 = Fraction(-1, 2)
    frac2 = Fraction(2, 3)
    result = frac1 * frac2
    assert result.numerator == -1
    assert result.denominator == 3  # -1/2 * 2/3 = -2/6 = -1/3

    # Test with positive and negative fractions
    frac1 = Fraction(1, 2)
    frac2 = Fraction(-2, 3)
    result = frac1 * frac2
    assert result.numerator == -1
    assert result.denominator == 3  # 1/2 * -2/3 = -2/6 = -1/3

    # Test with integer multiplication
    frac1 = Fraction(3, 4)
    result = frac1 * 2
    assert result.numerator == 3
    assert result.denominator == 2  # 3/4 * 2 = 6/4 = 3/2

    # Test with zero numerator
    frac1 = Fraction(0, 4)
    frac2 = Fraction(1, 4)
    result = frac1 * frac2
    assert result.numerator == 0
    assert result.denominator == 1  # 0/4 * 1/4 = 0

    # Test with zero fractions
    frac1 = Fraction(0, 4)
    frac2 = Fraction(0, 4)
    result = frac1 * frac2
    assert result.numerator == 0
    assert result.denominator == 1  # 0/4 * 0/4 = 0

    # Test with negative fraction and integer
    frac1 = Fraction(-1, 4)
    result = frac1 * 2
    assert result.numerator == -1
    assert result.denominator == 2  # -1/4 * 2 = -2/4 = -1/2

    # Test with large integers
    frac1 = Fraction(1000000000, 1000000001)
    frac2 = Fraction(2, 3)
    result = frac1 * frac2
    assert result.numerator == 2000000000
    assert result.denominator == 3000000003  # 1000000000/1000000001 * 2/3 = 2000000000/3000000003


def test_fraction_truediv_method():
    """
    Test the __truediv__ method of the Fraction class.
    """

    # Test with positive fractions
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)
    result = frac1 / frac2
    assert result.numerator == 3
    assert result.denominator == 4  # 1/2 / 2/3 = 1/2 * 3/2 = 3/4

    # Test with negative fractions
    frac1 = Fraction(-1, 2)
    frac2 = Fraction(2, 3)
    result = frac1 / frac2
    assert result.numerator == -3
    assert result.denominator == 4  # -1/2 / 2/3 = -1/2 * 3/2 = -3/4

    # Test with positive and negative fractions
    frac1 = Fraction(1, 2)
    frac2 = Fraction(-2, 3)
    result = frac1 / frac2
    assert result.numerator == -3
    assert result.denominator == 4  # 1/2 / -2/3 = 1/2 * -3/2 = -3/4

    # Test with integer division
    frac1 = Fraction(3, 4)
    result = frac1 / 2
    assert result.numerator == 3
    assert result.denominator == 8  # 3/4 / 2 = 3/4 * 1/2 = 3/8

    # Test with zero numerator
    frac1 = Fraction(0, 4)
    frac2 = Fraction(1, 4)
    result = frac1 / frac2
    assert result.numerator == 0
    assert result.denominator == 1  # 0/4 / 1/4 = 0

    # Test with zero fractions
    frac1 = Fraction(0, 4)
    frac2 = Fraction(0, 4)
    with pytest.raises(ValueError, match=r"Denominator cannot be zero"):
        result = frac1 / frac2  # 0/4 / 0/4 should raise ZeroDivisionError

    # Test with negative fraction and integer
    frac1 = Fraction(-1, 4)
    result = frac1 / 2
    assert result.numerator == -1
    assert result.denominator == 8  # -1/4 / 2 = -1/4 * 1/2 = -1/8

    # Test with large integers
    frac1 = Fraction(1000000000, 1000000001)
    frac2 = Fraction(2, 3)
    result = frac1 / frac2
    assert result.numerator == 1500000000
    assert result.denominator == 1000000001  # 1000000000/1000000001 / 2/3 = 1000000000/1000000001 * 3/2 = 3000000000/2000000002 = 1500000000/1000000001


def test_fraction_eq_method():
    """
    Test the __eq__ method of the Fraction class.
    """

    # Test equality of fractions with the same numerator and denominator
    frac1 = Fraction(1, 2)
    frac2 = Fraction(1, 2)
    assert frac1 == frac2  # 1/2 == 1/2

    # Test equality of fractions with different numerators and denominators but equivalent values
    frac1 = Fraction(2, 4)
    frac2 = Fraction(1, 2)
    assert frac1 == frac2  # 2/4 == 1/2

    # Test equality with fractions that reduce to the same value
    frac1 = Fraction(3, 9)
    frac2 = Fraction(1, 3)
    assert frac1 == frac2  # 3/9 == 1/3

    # Test equality with negative fractions
    frac1 = Fraction(-1, 2)
    frac2 = Fraction(1, -2)
    assert frac1 == frac2  # -1/2 == 1/-2

    # Test inequality with different fractions
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)
    assert frac1 != frac2  # 1/2 != 2/3

    # Test equality with zero fractions
    frac1 = Fraction(0, 1)
    frac2 = Fraction(0, 5)
    assert frac1 == frac2  # 0/1 == 0/5

    # Test inequality with zero numerator and non-zero numerator
    frac1 = Fraction(0, 1)
    frac2 = Fraction(1, 5)
    assert frac1 != frac2  # 0/1 != 1/5

    # Test equality with integer comparison
    frac1 = Fraction(4, 2)
    assert frac1 == 2  # 4/2 == 2

    # Test inequality with integer comparison
    frac1 = Fraction(3, 2)
    assert frac1 != 2  # 3/2 != 2

    # Test equality with large fractions
    frac1 = Fraction(1000000000, 2000000000)
    frac2 = Fraction(1, 2)
    assert frac1 == frac2  # 1000000000/2000000000 == 1/2

    # Test inequality with large fractions
    frac1 = Fraction(1000000000, 2000000000)
    frac2 = Fraction(2, 3)
    assert frac1 != frac2  # 1000000000/2000000000 != 2/3
    
def test_fraction_lt_method():
    """
    Test the __lt__ method of the Fraction class.
    """

    # Test with positive fractions
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)
    assert frac1 < frac2  # 1/2 < 2/3

    # Test with negative fractions
    frac1 = Fraction(-1, 2)
    frac2 = Fraction(2, 3)
    assert frac1 < frac2  # -1/2 < 2/3

    # Test with positive and negative fractions
    frac1 = Fraction(1, 2)
    frac2 = Fraction(-2, 3)
    assert not frac1 < frac2  # 1/2 is not < -2/3

    # Test with fractions having the same value
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 4)
    assert not frac1 < frac2  # 1/2 is not < 2/4

    # Test with zero numerator
    frac1 = Fraction(0, 1)
    frac2 = Fraction(1, 4)
    assert frac1 < frac2  # 0/1 < 1/4

    # Test with both fractions having zero numerator
    frac1 = Fraction(0, 4)
    frac2 = Fraction(0, 5)
    assert not frac1 < frac2  # 0/4 is not < 0/5

    # Test with integer comparison
    frac1 = Fraction(1, 2)
    assert frac1 < 1  # 1/2 < 1

    # Test with reverse integer comparison
    frac1 = Fraction(3, 2)
    assert not frac1 < 1  # 3/2 is not < 1

    # Test with large fractions
    frac1 = Fraction(1000000000, 2000000000)
    frac2 = Fraction(1, 2)
    assert not frac1 < frac2  # 1000000000/2000000000 is not < 1/2

    # Test with unequal large fractions
    frac1 = Fraction(1000000000, 3000000000)
    frac2 = Fraction(1, 2)
    assert frac1 < frac2  # 1000000000/3000000000 < 1/2

def test_fraction_le_method():
    """
    Test the __le__ method of the Fraction class.
    """

    # Test with positive fractions
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)
    assert frac1 <= frac2  # 1/2 <= 2/3

    # Test with negative fractions
    frac1 = Fraction(-1, 2)
    frac2 = Fraction(2, 3)
    assert frac1 <= frac2  # -1/2 <= 2/3

    # Test with positive and negative fractions
    frac1 = Fraction(1, 2)
    frac2 = Fraction(-2, 3)
    assert not frac1 <= frac2  # 1/2 is not <= -2/3

    # Test with fractions having the same value
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 4)
    assert frac1 <= frac2  # 1/2 <= 2/4

    # Test with zero numerator
    frac1 = Fraction(0, 1)
    frac2 = Fraction(1, 4)
    assert frac1 <= frac2  # 0/1 <= 1/4

    # Test with both fractions having zero numerator
    frac1 = Fraction(0, 4)
    frac2 = Fraction(0, 5)
    assert frac1 <= frac2  # 0/4 <= 0/5

    # Test with integer comparison
    frac1 = Fraction(1, 2)
    assert frac1 <= 1  # 1/2 <= 1

    # Test with reverse integer comparison
    frac1 = Fraction(3, 2)
    assert not frac1 <= 1  # 3/2 is not <= 1

    # Test with large fractions
    frac1 = Fraction(1000000000, 2000000000)
    frac2 = Fraction(1, 2)
    assert frac1 <= frac2  # 1000000000/2000000000 <= 1/2

    # Test with unequal large fractions
    frac1 = Fraction(1000000000, 3000000000)
    frac2 = Fraction(1, 2)
    assert frac1 <= frac2  # 1000000000/3000000000 <= 1/2

def test_fraction_simplify_method():
    """
    Test the simplify method of the Fraction class.
    """

    # Test simplifying a fraction with common factors
    frac = Fraction(4, 8)
    frac.simplify()
    assert frac.numerator == 1
    assert frac.denominator == 2  # 4/8 simplifies to 1/2

    # Test simplifying a fraction with no common factors
    frac = Fraction(3, 7)
    frac.simplify()
    assert frac.numerator == 3
    assert frac.denominator == 7  # 3/7 simplifies to 3/7 (unchanged)

    # Test simplifying a fraction with negative numerator
    frac = Fraction(-6, 9)
    frac.simplify()
    assert frac.numerator == -2
    assert frac.denominator == 3  # -6/9 simplifies to -2/3

    # Test simplifying a fraction with negative denominator
    frac = Fraction(6, -9)
    frac.simplify()
    assert frac.numerator == -2
    assert frac.denominator == 3  # 6/-9 simplifies to -2/3

    # Test simplifying a fraction with both negative numerator and denominator
    frac = Fraction(-6, -9)
    frac.simplify()
    assert frac.numerator == 2
    assert frac.denominator == 3  # -6/-9 simplifies to 2/3

    # Test simplifying a fraction that is already in simplest form
    frac = Fraction(1, 2)
    frac.simplify()
    assert frac.numerator == 1
    assert frac.denominator == 2  # 1/2 simplifies to 1/2 (unchanged)

    # Test simplifying a fraction with zero numerator
    frac = Fraction(0, 5)
    frac.simplify()
    assert frac.numerator == 0
    assert frac.denominator == 1  # 0/5 simplifies to 0/1

    # Test simplifying a large fraction
    frac = Fraction(1000000, 2000000)
    frac.simplify()
    assert frac.numerator == 1
    assert frac.denominator == 2  # 1000000/2000000 simplifies to 1/2

def test_fraction_to_decimal_method():
    """
    Test the to_decimal method of the Fraction class.
    """

    # Test converting a simple fraction to decimal
    frac = Fraction(1, 2)
    assert frac.to_decimal() == 0.5  # 1/2 should be 0.5

    # Test converting a negative fraction to decimal
    frac = Fraction(-1, 2)
    assert frac.to_decimal() == -0.5  # -1/2 should be -0.5

    # Test converting a fraction with a negative denominator to decimal
    frac = Fraction(1, -2)
    assert frac.to_decimal() == -0.5  # 1/-2 should be -0.5

    # Test converting a fraction with both negative numerator and denominator to decimal
    frac = Fraction(-1, -2)
    assert frac.to_decimal() == 0.5  # -1/-2 should be 0.5

    # Test converting a fraction with zero numerator to decimal
    frac = Fraction(0, 5)
    assert frac.to_decimal() == 0.0  # 0/5 should be 0.0

    # Test converting a whole number fraction to decimal
    frac = Fraction(4, 2)
    assert frac.to_decimal() == 2.0  # 4/2 should be 2.0

    # Test converting a large fraction to decimal
    frac = Fraction(1000000, 2000000)
    assert frac.to_decimal() == 0.5  # 1000000/2000000 should be 0.5

    # Test converting an improper fraction to decimal
    frac = Fraction(7, 3)
    assert frac.to_decimal() == 7 / 3  # 7/3 should be 7/3 (or 2.333...)

    # Test converting a fraction to decimal where numerator is greater than denominator
    frac = Fraction(9, 4)
    assert frac.to_decimal() == 2.25  # 9/4 should be 2.25

@pytest.fixture
def sample_fraction():
    # Fixture to provide a sample Fraction object for testing
    return Fraction(3, 5)

def test_fraction_reciprocal_method(sample_fraction):
    # Test case 1: Basic functionality
    reciprocal_fraction = sample_fraction.reciprocal()
    assert reciprocal_fraction.numerator == sample_fraction.denominator
    assert reciprocal_fraction.denominator == sample_fraction.numerator

    # Test case 2: Reciprocal of a reciprocal should return the original fraction
    double_reciprocal = reciprocal_fraction.reciprocal()
    assert double_reciprocal.numerator == sample_fraction.numerator
    assert double_reciprocal.denominator == sample_fraction.denominator

    # Test case 3: Identity test for original fraction after reciprocal
    assert sample_fraction.numerator == 3
    assert sample_fraction.denominator == 5

    # Test case 4: Edge case with large numbers
    large_fraction = Fraction(987654321, 123456789)
    large_reciprocal = large_fraction.reciprocal()
    assert large_reciprocal.numerator == large_fraction.denominator
    assert large_reciprocal.denominator == large_fraction.numerator

    # Test case 5: Zero numerator and non-zero denominator
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        zero_numerator = Fraction(0, 7)
        zero_reciprocal = zero_numerator.reciprocal()

    # Test case 7: Negative numerator and positive denominator
    negative_fraction = Fraction(-4, 9)
    negative_reciprocal = negative_fraction.reciprocal()
    assert negative_reciprocal.numerator == 9
    assert negative_reciprocal.denominator == -4

    # Test case 8: Positive numerator and negative denominator
    negative_denominator = Fraction(5, -2)
    negative_denom_reciprocal = negative_denominator.reciprocal()
    assert negative_denom_reciprocal.numerator == -2
    assert negative_denom_reciprocal.denominator == 5
    
def test_fraction_from_decimal_method():
    # Test case 1: Basic functionality with default precision
    fraction = Fraction.from_decimal(0.5)
    assert fraction.numerator == 1
    assert fraction.denominator == 2

    # Test case 2: Higher precision for accuracy
    fraction_precise = Fraction.from_decimal(0.123456789, precision=9)
    assert fraction_precise.numerator == 123456789
    assert fraction_precise.denominator == 1000000000

    # Test case 3: Negative decimal number
    negative_fraction = Fraction.from_decimal(-0.75)
    assert negative_fraction.numerator == -7
    assert negative_fraction.denominator == 10

    # Test case 4: Zero decimal number
    zero_fraction = Fraction.from_decimal(0.0)
    assert zero_fraction.numerator == 0
    assert zero_fraction.denominator == 1

    # Test case 5: Decimal number with very high precision
    high_precision_fraction = Fraction.from_decimal(0.1234567890123456789, precision=18)
    assert high_precision_fraction.numerator == 1543209862654321
    assert high_precision_fraction.denominator == 12500000000000000


def test_fraction_abs_method():
    
    negative_int = Fraction(-1, 1)
    p_negative_int = abs(negative_int)
    assert p_negative_int.numerator == 1
    assert p_negative_int.denominator == 1
    assert p_negative_int == 1
    
    negative_fraction = Fraction(-3, 7)
    p_negative_fraction = abs(negative_fraction)
    assert p_negative_fraction.denominator == 7
    assert p_negative_fraction.numerator == 3
    
def test_fraction_floor_method():
    # Test case 1: Positive fraction
    positive_fraction = Fraction(7, 3)
    assert math.floor(positive_fraction) == Fraction(2, 1)

    # Test case 2: Negative fraction
    negative_fraction = Fraction(-7, 3)
    assert math.floor(negative_fraction) == Fraction(-3, 1)

    # Test case 3: Fraction resulting in zero
    zero_fraction = Fraction(1, 3)
    assert math.floor(zero_fraction) == Fraction(0, 1)

    # Test case 4: Fraction equal to an integer
    integer_fraction = Fraction(6, 2)
    assert math.floor(integer_fraction) == Fraction(3, 1)

    # Test case 5: Small positive fraction
    small_positive_fraction = Fraction(1, 10)
    assert math.floor(small_positive_fraction) == Fraction(0, 1)

    # Test case 6: Small negative fraction
    small_negative_fraction = Fraction(-1, 10)
    assert math.floor(small_negative_fraction) == Fraction(-1, 1)

    # Test case 7: Large positive fraction
    large_positive_fraction = Fraction(123456789, 1000000)
    assert math.floor(large_positive_fraction) == Fraction(123, 1)

    # Test case 8: Large negative fraction
    large_negative_fraction = Fraction(-123456789, 1000000)
    assert math.floor(large_negative_fraction) == Fraction(-124, 1)



def test_fraction_ceil_method():
    # Test case 1: Positive fraction
    positive_fraction = Fraction(7, 3)
    assert math.ceil(positive_fraction) == Fraction(3, 1)

    # Test case 2: Negative fraction
    negative_fraction = Fraction(-7, 3)
    assert math.ceil(negative_fraction) == Fraction(-2, 1)

    # Test case 3: Fraction resulting in zero
    zero_fraction = Fraction(1, 3)
    assert math.ceil(zero_fraction) == Fraction(1, 1)

    # Test case 4: Fraction equal to an integer
    integer_fraction = Fraction(6, 2)
    assert math.ceil(integer_fraction) == Fraction(3, 1)

    # Test case 5: Small positive fraction
    small_positive_fraction = Fraction(1, 10)
    assert math.ceil(small_positive_fraction) == Fraction(1, 1)

    # Test case 6: Small negative fraction
    small_negative_fraction = Fraction(-1, 10)
    assert math.ceil(small_negative_fraction) == Fraction(0, 1)

    # Test case 7: Large positive fraction
    large_positive_fraction = Fraction(123456789, 1000000)
    assert math.ceil(large_positive_fraction) == Fraction(124, 1)

    # Test case 8: Large negative fraction
    large_negative_fraction = Fraction(-123456789, 1000000)
    assert math.ceil(large_negative_fraction) == Fraction(-123, 1)

def test_fraction_round_method():
    # Test case 1: Positive fraction rounding down
    positive_fraction_down = Fraction(7, 3)
    assert round(positive_fraction_down) == Fraction(2, 1)

    # Test case 2: Positive fraction rounding up
    positive_fraction_up = Fraction(8, 3)
    assert round(positive_fraction_up) == Fraction(3, 1)

    # Test case 3: Negative fraction rounding down
    negative_fraction_down = Fraction(-7, 3)
    assert round(negative_fraction_down) == Fraction(-2, 1)

    # Test case 4: Negative fraction rounding up
    negative_fraction_up = Fraction(-8, 3)
    assert round(negative_fraction_up) == Fraction(-3, 1)

    # Test case 5: Fraction resulting in zero
    zero_fraction = Fraction(1, 3)
    assert round(zero_fraction) == Fraction(0, 1)

    # Test case 6: Fraction equal to an integer
    integer_fraction = Fraction(6, 2)
    assert round(integer_fraction) == Fraction(3, 1)

    # Test case 7: Small positive fraction
    small_positive_fraction = Fraction(1, 10)
    assert round(small_positive_fraction) == Fraction(0, 1)

    # Test case 8: Small negative fraction
    small_negative_fraction = Fraction(-1, 10)
    assert round(small_negative_fraction) == Fraction(0, 1)

    # Test case 9: Large positive fraction rounding down
    large_positive_fraction_down = Fraction(123456789, 1000000)
    assert round(large_positive_fraction_down) == Fraction(123, 1)

    # Test case 10: Large positive fraction rounding up
    large_positive_fraction_up = Fraction(123500000, 1000000)
    assert round(large_positive_fraction_up) == Fraction(124, 1)

    # Test case 11: Large negative fraction rounding down
    large_negative_fraction_down = Fraction(-123456789, 1000000)
    assert round(large_negative_fraction_down) == Fraction(-123, 1)

    # Test case 12: Large negative fraction rounding up
    large_negative_fraction_up = Fraction(-123500000, 1000000)
    assert round(large_negative_fraction_up) == Fraction(-124, 1)


def test_fraction_iadd_method():
    # Test case 1: Positive fractions
    x = Fraction(1, 2)
    y = Fraction(1, 3)
    x += y
    assert x == Fraction(5, 6)

    # Test case 2: Negative fractions
    x = Fraction(-1, 2)
    y = Fraction(-1, 3)
    x += y
    assert x == Fraction(-5, 6)

    # Test case 3: Positive and negative fractions
    x = Fraction(1, 2)
    y = Fraction(-1, 3)
    x += y
    assert x == Fraction(1, 6)

    # Test case 4: Fraction and integer
    x = Fraction(3, 4)
    y = Fraction(2, 1)  # Equivalent to integer 2
    x += y
    assert x == Fraction(11, 4)

    # Test case 5: Integer and fraction
    x = Fraction(5, 1)  # Equivalent to integer 5
    y = Fraction(1, 3)
    x += y
    assert x == Fraction(16, 3)

    # Test case 6: Zero addition
    x = Fraction(0, 1)
    y = Fraction(1, 2)
    x += y
    assert x == Fraction(1, 2)

    # Test case 7: Adding zero
    x = Fraction(3, 4)
    y = Fraction(0, 1)
    x += y
    assert x == Fraction(3, 4)

    # Test case 8: Adding to itself
    x = Fraction(1, 2)
    x += x
    assert x == Fraction(1, 1)
    
    # Test case 9: Large numbers
    x = Fraction(987654321, 123456789)
    y = Fraction(123456789, 987654321)
    x += y
    expected_numerator = 987654321 * 987654321 + 123456789 * 123456789
    expected_denominator = 123456789 * 987654321
    assert x == Fraction(expected_numerator, expected_denominator, True)

def test_fraction_isub_method():
    # Test case 1: Positive fractions
    x = Fraction(5, 6)
    y = Fraction(1, 3)
    x -= y
    assert x == Fraction(1, 2)

    # Test case 2: Negative fractions
    x = Fraction(-5, 6)
    y = Fraction(-1, 3)
    x -= y
    assert x == Fraction(-1, 2)

    # Test case 3: Positive and negative fractions
    x = Fraction(1, 2)
    y = Fraction(-1, 3)
    x -= y
    assert x == Fraction(5, 6)

    # Test case 4: Fraction and integer
    x = Fraction(11, 4)
    y = Fraction(2, 1)  # Equivalent to integer 2
    x -= y
    assert x == Fraction(3, 4)

    # Test case 5: Integer and fraction
    x = Fraction(16, 3)  # Equivalent to integer 5
    y = Fraction(1, 3)
    x -= y
    assert x == Fraction(5, 1)

    # Test case 6: Zero subtraction
    x = Fraction(1, 2)
    y = Fraction(0, 1)
    x -= y
    assert x == Fraction(1, 2)

    # Test case 7: Subtracting zero
    x = Fraction(3, 4)
    y = Fraction(0, 1)
    x -= y
    assert x == Fraction(3, 4)

    # Test case 8: Subtracting from itself
    x = Fraction(1, 2)
    x -= x
    assert x == Fraction(0, 1)

    # Test case 9: Large numbers
    x = Fraction(987654321, 123456789)
    y = Fraction(123456789, 987654321)
    x -= y
    expected_numerator = 987654321 * 987654321 - 123456789 * 123456789
    expected_denominator = 123456789 * 987654321
    assert x == Fraction(expected_numerator, expected_denominator, True)


def test_fraction_imul_method():
    # Test case 1: Positive fractions
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    x *= y
    assert x == Fraction(1, 3)

    # Test case 2: Negative fractions
    x = Fraction(-1, 2)
    y = Fraction(-2, 3)
    x *= y
    assert x == Fraction(1, 3)

    # Test case 3: Positive and negative fractions
    x = Fraction(1, 2)
    y = Fraction(-2, 3)
    x *= y
    assert x == Fraction(-1, 3)

    # Test case 4: Fraction and integer
    x = Fraction(3, 4)
    y = Fraction(2, 1)  # Equivalent to integer 2
    x *= y
    assert x == Fraction(3, 2)

    # Test case 5: Integer and fraction
    x = Fraction(5, 1)  # Equivalent to integer 5
    y = Fraction(1, 3)
    x *= y
    assert x == Fraction(5, 3)

    # Test case 6: Multiplying by zero
    x = Fraction(2, 3)
    y = Fraction(0, 1)
    x *= y
    assert x == Fraction(0, 1)

    # Test case 7: Multiplying by one
    x = Fraction(3, 4)
    y = Fraction(1, 1)
    x *= y
    assert x == Fraction(3, 4)

    # Test case 8: Large numbers
    x = Fraction(987654321, 123456789)
    y = Fraction(123456789, 987654321)
    x *= y
    expected_numerator = 987654321 * 123456789
    expected_denominator = 123456789 * 987654321
    assert x == Fraction(expected_numerator, expected_denominator, True)
    
    
def test_fraction_itruediv_method():
    # Test case 1: Positive fractions
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    x /= y
    assert x == Fraction(3, 4)

    # Test case 2: Negative fractions
    x = Fraction(-1, 2)
    y = Fraction(-2, 3)
    x /= y
    assert x == Fraction(3, 4)

    # Test case 3: Positive and negative fractions
    x = Fraction(1, 2)
    y = Fraction(-2, 3)
    x /= y
    assert x == Fraction(-3, 4)

    # Test case 4: Fraction and integer
    x = Fraction(3, 4)
    y = Fraction(2, 1)  # Equivalent to integer 2
    x /= y
    assert x == Fraction(3, 8)

    # Test case 5: Integer and fraction
    x = Fraction(5, 1)  # Equivalent to integer 5
    y = Fraction(1, 3)
    x /= y
    assert x == Fraction(15, 1)

    # Test case 6: Division by zero (should raise ZeroDivisionError)
    x = Fraction(2, 3)
    y = Fraction(0, 1)
    
    with pytest.raises(ValueError, match=r"Denominator cannot be zero"):
        result = x / y  # should raise ZeroDivisionError

    # Test case 7: Division by one
    x = Fraction(3, 4)
    y = Fraction(1, 1)
    x /= y
    assert x == Fraction(3, 4)

    # Test case 8: Large numbers
    x = Fraction(987654321, 123456789)
    y = Fraction(123456789, 987654321)
    x /= y
    expected_numerator = 987654321 * 987654321
    expected_denominator = 123456789 * 123456789
    assert x == Fraction(expected_numerator, expected_denominator, True)


def test_fraction_pow_method():
    # Test case 1: Positive exponent
    x = Fraction(2, 3)
    y = 3
    result = x ** y
    assert result == Fraction(8, 27)

    # Test case 2: Negative exponent
    x = Fraction(2, 3)
    y = -2
    result = x ** y
    assert result == Fraction(9, 4)

    # Test case 3: Zero exponent
    x = Fraction(2, 3)
    y = 0
    result = x ** y
    assert result == Fraction(1, 1)

    # Test case 4: Fractional base with positive integer exponent
    x = Fraction(3, 4)
    y = 2
    result = x ** y
    assert result == Fraction(9, 16)

    # Test case 5: Fractional base with negative integer exponent
    x = Fraction(3, 4)
    y = -2
    result = x ** y
    assert result == Fraction(16, 9)

    # Test case 6: Integer base with positive exponent
    x = Fraction(5, 1)  # Equivalent to integer 5
    y = 3
    result = x ** y
    assert result == Fraction(125, 1)

    # Test case 7: Integer base with negative exponent
    x = Fraction(5, 1)  # Equivalent to integer 5
    y = -1
    result = x ** y
    assert result == Fraction(1, 5)

    # Test case 8: Zero base with positive exponent
    x = Fraction(0, 1)
    y = 5
    result = x ** y
    assert result == Fraction(0, 1)

    # Test case 9: Zero base with zero exponent (should be 1)
    x = Fraction(0, 1)
    y = 0
    result = x ** y
    assert result == Fraction(1, 1)

    # Test case 10: Large exponent
    x = Fraction(2, 3)
    y = 10
    result = x ** y
    assert result == Fraction(1024, 59049)


# Run the tests
if __name__ == "__main__":
    pytest.main()
