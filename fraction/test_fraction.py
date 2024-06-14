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

    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        Fraction(3, 0)
        
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        Fraction(5, 0)
        

# Run the tests
if __name__ == "__main__":
    pytest.main()
