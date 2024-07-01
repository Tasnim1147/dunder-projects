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

    def __init__(
        self,
        a: int,
        b: int,
        simplify: bool = False,
    ) -> None:
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
        if simplify:
            self.simplify()

    def __str__(
        self,
    ) -> str:
        """
        Returns a string representation of the fraction.

        Returns
        -------
        str
            A string in the form 'numerator/denominator'.
        """
        return self.__repr__()

    # Future Methods:
    def __repr__(
        self,
    ) -> str:
        """
        Returns a string representation of the fraction for debugging purposes.

        Returns
        -------
        str
            A string representation for debugging.
        """
        if self.numerator == 0:
            return "0"
        elif self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def __add__(
        self,
        other: "Fraction",
    ) -> "Fraction":
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
                new_numerator = (
                    self.numerator * other.denominator
                    + other.numerator * self.denominator
                )
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
            raise TypeError(
                "Unsupported operand types for +: 'Fraction' and '{}'".format(
                    type(other).__name__
                )
            )

    def __iadd__(
        self,
        other: "Fraction",
    ) -> "Fraction":
        """
        In-place add method to add another Fraction to the current Fraction object.

        Parameters:
            other (Fraction): The Fraction object to add to the current Fraction.

        Returns:
            Fraction: The updated current Fraction object after addition.
        """
        _temp = self.__add__(other)
        self.numerator = _temp.numerator
        self.denominator = _temp.denominator
        self.simplify()
        return self

    def __radd__(
        self,
        other: "Fraction",
    ) -> "Fraction":
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

    def __sub__(
        self,
        other: "Fraction",
    ) -> "Fraction":
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

        new_numerator = (
            self.numerator * other.denominator
            - self.denominator * other.numerator
        )
        if new_numerator == 0:
            new_denominator = self.denominator
        else:
            new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator, True)

    def __isub__(
        self,
        other: "Fraction",
    ) -> "Fraction":
        """
        Subtracts another fraction from the current fraction and updates the numerator and denominator attributes of the current fraction.

        Parameters:
            other (Fraction): The fraction to subtract.

        Returns:
            Fraction: The updated current fraction after subtraction.
        """
        _temp = self.__sub__(other)
        self.numerator = _temp.numerator
        self.denominator = _temp.denominator
        return self

    def __mul__(
        self,
        other: "Fraction",
    ) -> "Fraction":
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

    def __imul__(
        self,
        other: "Fraction",
    ) -> "Fraction":
        """
        Multiply the current Fraction object by another Fraction object in-place.

        Args:
            other (Fraction): The Fraction object to multiply with.

        Returns:
            Fraction: The updated current Fraction object after the multiplication.

        Example:
            >>> fraction1 = Fraction(2, 3)
            >>> fraction2 = Fraction(4, 5)
            >>> fraction1 *= fraction2
            >>> print(fraction1)
            Fraction(8, 15)
        """
        _temp = self.__mul__(other)
        self.numerator = _temp.numerator
        self.denominator = _temp.denominator
        return self

    def __truediv__(
        self,
        other: "Fraction",
    ) -> "Fraction":
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

    def __itruediv__(
        self,
        other: "Fraction",
    ) -> "Fraction":
        """
        Divides one fraction by another in-place and updates the current fraction with the result.

        Parameters
        ----------
        other : Fraction
            The fraction to divide by.

        Returns
        -------
        Fraction
            The current fraction after division.
        """
        _temp = self.__truediv__(other)
        self.numerator = _temp.numerator
        self.denominator = _temp.denominator
        return self

    def __pow__(
        self,
        other: int,
    ) -> "Fraction":
        """
        Raises the current fraction to the power of the given integer.

        Parameters
        ----------
        other : int
            The exponent to raise the fraction to.

        Returns
        -------
        Fraction
            A new Fraction object representing the result of the exponentiation.
        """
        return Fraction(self.numerator**other, self.denominator**other)

    def __ipow__(
        self,
        other: int,
    ) -> "Fraction":
        """
        Raises the current fraction to the power of the input integer and updates the current fraction with the result.

        Parameters:
            other (int): The power to raise the current fraction to.

        Returns:
            Fraction: The updated current fraction after exponentiation.
        """
        _temp = self**other
        self.numerator = _temp.numerator
        self.denominator = _temp.denominator
        return self

    def __eq__(
        self,
        other: "Fraction",
    ) -> bool:
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
        return (
            self.numerator * other.denominator
            == self.denominator * other.numerator
        )

    def __lt__(
        self,
        other: "Fraction",
    ) -> bool:
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
        return (
            self.numerator * other.denominator
            < self.denominator * other.numerator
        )

    def __le__(
        self,
        other: "Fraction",
    ) -> bool:
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
        return (
            self.numerator * other.denominator
            <= self.denominator * other.numerator
        )

    def __abs__(
        self,
    ) -> "Fraction":
        """
        Returns a new Fraction object with the absolute values of the numerator and denominator of the current Fraction object.

        :return: A new Fraction object with the absolute values of the numerator and denominator of the current Fraction object.
        :rtype: Fraction
        """
        return Fraction(abs(self.numerator), abs(self.denominator))

    def __floor__(
        self,
    ) -> "Fraction":
        """
        Returns a new Fraction object representing the floor of the decimal value of this Fraction.

        :return: A new Fraction object.
        :rtype: Fraction
        """
        return Fraction(math.floor(self.to_decimal()), 1)

    def __ceil__(
        self,
    ) -> "Fraction":
        """
        Returns a new Fraction object that represents the ceiling of the current Fraction object.

        This method calculates the ceiling of the decimal representation of the current Fraction object using the `math.ceil` function and creates a new Fraction object with the rounded-up numerator and a denominator of 1.

        Returns:
            Fraction: A new Fraction object representing the ceiling of the current Fraction object.
        """
        return Fraction(math.ceil(self.to_decimal()), 1)

    def __round__(
        self,
    ) -> "Fraction":
        """
        Returns a new Fraction object that represents the rounded value of the current Fraction object.
        This method rounds the decimal representation of the current Fraction object using the `round` function and creates a new Fraction object with the rounded numerator and a denominator of 1.

        Returns:
            Fraction: A new Fraction object representing the rounded value of the current Fraction object.
        """
        return Fraction(round(self.to_decimal()), 1)

    def simplify(
        self,
    ) -> None:
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

    def reciprocal(
        self,
    ) -> "Fraction":
        """
        Returns a new Fraction object that is the reciprocal of the current Fraction object.

        Returns:
            Fraction: The reciprocal of the current Fraction object.
        """
        return Fraction(self.denominator, self.numerator, simplify=False)

    def to_decimal(
        self,
    ) -> float:
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
    def from_decimal(
        cls,
        decimal: float,
        precision: int = 1,
    ) -> "Fraction":
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
        numerator = int(decimal * (10**precision))
        denominator = 10**precision
        return cls(numerator, denominator, simplify=True)
