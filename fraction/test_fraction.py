import pytest
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



# Run the tests
if __name__ == "__main__":
    pytest.main()
