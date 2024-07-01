import math


class Fraction:
    """
    A class to represent a fraction with a numerator and a denominator.
    
    Attributes
    ----------
    numerator : int
        The numerator of the fraction.
    denominator : int
        The denominator of the fraction.
    
    Methods
    -------
    __init__(self, a: int, b: int) -> None:
        Constructs a Fraction object with the given numerator and denominator.
        
    __str__(self) -> str:
        Returns a string representation of the fraction in the form 'numerator/denominator'.
    
    __repr__(self) -> str:
        Returns a string representation of the fraction for debugging purposes.
    
    __add__(self, other: 'Fraction') -> 'Fraction':
        Adds two fractions (self + other) and returns the result as a new Fraction object.
        
    __radd__(self, other: 'Fraction') -> 'Fraction':
        Adds two fractions (other + self) and returns the result as a new Fraction object.
    
    __sub__(self, other: 'Fraction') -> 'Fraction':
        Subtracts one fraction from another and returns the result as a new Fraction object.
    
    __mul__(self, other: 'Fraction') -> 'Fraction':
        Multiplies two fractions and returns the result as a new Fraction object.
    
    __truediv__(self, other: 'Fraction') -> 'Fraction':
        Divides one fraction by another and returns the result as a new Fraction object.
    
    __eq__(self, other: 'Fraction') -> bool:
        Checks if two fractions are equal.
    
    __lt__(self, other: 'Fraction') -> bool:
        Checks if one fraction is less than another.
    
    __le__(self, other: 'Fraction') -> bool:
        Checks if one fraction is less than or equal to another.
    
    simplify(self) -> 'Fraction':
        Simplifies the fraction to its lowest terms.
    
    to_decimal(self) -> float:
        Converts the fraction to its decimal representation.
    
    from_decimal(cls, decimal: float) -> 'Fraction':
        Class method to create a Fraction object from a decimal.
    
    """

    def __init__(self, a: int, b: int, simplify: bool = False) -> None:
        """
        Constructs a Fraction object with the given numerator and denominator.
        
        Parameters
        ----------
        a : int
            The numerator of the fraction.
        b : int
            The denominator of the fraction.
        
        Raises
        ------
        ValueError
            If the denominator is zero.
        """
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = a 
        self.denominator = b
        if simplify: self.simplify()
        
    def __str__(self) -> str:
        """
        Returns a string representation of the fraction.
        
        Returns
        -------
        str
            A string in the form 'numerator/denominator'.
        """
        return self.__repr__()
        
    
    # Future Methods:
    def __repr__(self) -> str:
        """
        Returns a string representation of the fraction for debugging purposes.
        
        Returns
        -------
        str
            A string representation for debugging.
        """
        if self.numerator == 0: return "0"
        elif self.denominator == 1: return f'{self.numerator}' 
        return f'{self.numerator}/{self.denominator}'
    
    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Adds two fractions and returns the result as a new Fraction object.
        
        Parameters
        ----------
        other : Fraction
            The fraction to add.
        
        Returns
        -------
        Fraction
            The result of the addition.
        """
        if isinstance(other, Fraction):
            if self.denominator != other.denominator:
                new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
                new_denominator = self.denominator * other.denominator
            else:
                new_numerator = self.numerator + other.numerator
                new_denominator = self.denominator
            return Fraction(new_numerator, new_denominator, True) 
        elif isinstance(other, int): 
            new_numerator = self.numerator + other * self.denominator
            new_denominator = self.denominator
            return Fraction(new_numerator, new_denominator, True) 
        else:
            raise TypeError("Unsupported operand types for +: 'Fraction' and '{}'".format(type(other).__name__))
        
    def __iadd__(self, other: 'Fraction') -> 'Fraction':
        _temp = self.__add__(other)
        self.numerator = _temp.numerator
        self.denominator = _temp.denominator
        self.simplify()
        return self
        
    def __radd__(self, other: 'Fraction') -> 'Fraction':
        """
        Adds two fractions (other + self) and returns the result as a new Fraction object.
        
        Parameters
        ----------
        other : Fraction
            The fraction to add.
        
        Returns
        -------
        Fraction
            The result of the addition.
        """
        return self.__add__(other)
        
    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Subtracts one fraction from another and returns the result as a new Fraction object.
        
        Parameters
        ----------
        other : Fraction
            The fraction to subtract.
        
        Returns
        -------
        Fraction
            The result of the subtraction.
        """

        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        if new_numerator == 0:
            new_denominator = self.denominator
        else: new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator, True)
    
    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Multiplies two fractions and returns the result as a new Fraction object.
        
        Parameters
        ----------
        other : Fraction
            The fraction to multiply.
        
        Returns
        -------
        Fraction
            The result of the multiplication.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator, True)
    
    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """
        Divides one fraction by another and returns the result as a new Fraction object.
        
        Parameters
        ----------
        other : Fraction
            The fraction to divide by.
        
        Returns
        -------
        Fraction
            The result of the division.
        """
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator, True)
    
    def __eq__(self, other: 'Fraction') -> bool:
        """
        Checks if two fractions are equal.
        
        Parameters
        ----------
        other : Fraction
            The fraction to compare.
        
        Returns
        -------
        bool
            True if the fractions are equal, False otherwise.
        """
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __lt__(self, other: 'Fraction') -> bool:
        """
        Checks if one fraction is less than another.
        
        Parameters
        ----------
        other : Fraction
            The fraction to compare.
        
        Returns
        -------
        bool
            True if this fraction is less than the other fraction, False otherwise.
        """
        return self.numerator * other.denominator < self.denominator * other.numerator
    
    def __le__(self, other: 'Fraction') -> bool:
        """
        Checks if one fraction is less than or equal to another.
        
        Parameters
        ----------
        other : Fraction
            The fraction to compare.
        
        Returns
        -------
        bool
            True if this fraction is less than or equal to the other fraction, False otherwise.
        """
        return self.numerator * other.denominator <= self.denominator * other.numerator
    
    
    def __abs__(self) -> 'Fraction':
        return Fraction(abs(self.numerator), abs(self.denominator))
    
    def __floor__(self) -> 'Fraction':
        return Fraction(math.floor(self.to_decimal()), 1)
    
    def __ceil__(self) -> 'Fraction':
        return Fraction(math.ceil(self.to_decimal()), 1)
    
    def __round__(self) -> 'Fraction':
        return Fraction(round(self.to_decimal()), 1)
    
    def simplify(self) -> None:
        """
        Simplifies the fraction to its lowest terms.
    
        Example:
        --------
        4/8 becomes 1/2
        """
        
        if self.numerator < 0 and self.denominator < 0:
            self.numerator = abs(self.numerator)
            self.denominator = abs(self.denominator)
        
        if self.numerator > 0 and self.denominator < 0:
            self.denominator = abs(self.denominator)
            self.numerator = -1 * self.numerator
            
        if self.numerator == 0: 
            self.denominator = 1
            return
        
        divisor = math.gcd(self.numerator, self.denominator)
        
        self.numerator = self.numerator // divisor
        self.denominator = self.denominator // divisor
        
    
    
    def reciprocal(self) -> 'Fraction':
        """
        Returns the reciprocal of the fraction.
        """
        return Fraction(self.denominator, self.numerator, simplify=False)
    
    def to_decimal(self) -> float:
        """
        Converts the fraction to its decimal representation.
    
        Returns:
        --------
        float
            The decimal representation of the fraction.
            
        Example:
        --------
        1/2 returns 0.5
        """
        return self.numerator / self.denominator
    
    @classmethod
    def from_decimal(cls, decimal: float, precision: int = 1) -> 'Fraction':
        """
        Creates a Fraction object from a floating-point decimal number.
    
        Parameters
        ----------
        decimal : float
            The decimal number to convert into a Fraction object.
        precision : int, optional
            The precision to use during conversion (default is 1).
        
        Returns
        -------
        Fraction
            A new Fraction object representing the equivalent fraction of the decimal.
        
        Notes
        -----
        The `precision` parameter determines the number of decimal places to consider
        during conversion. Increasing precision may lead to a more accurate Fraction
        representation, but may not eliminate floating-point approximation completely.
        """
        numerator = int(decimal * (10 ** precision))
        denominator = 10 ** precision
        return cls(numerator, denominator, simplify=True)
    
    
    
    
        