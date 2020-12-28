class calculator:
    """
    A class to perfrom basic calculator functions.
    ...
    Attributes
    ----------
    number : float
        an integer or floating digit as default value

    Methods
    -------
    getNumber():
        Returns the current value of calculator
    reset():
        Resets calculator's memory to 0
    add(input):
        Returns sum of number and input
    subtract(input):
        Returns difference between number and input
    multiply(input):
        Returns product of number and input
    division(input):
        Returns quotient of number and input
    nroot(n):
        Returns nth root of number
    """
    def __init__(self, number = 0) -> None:
        """
        Constructs a necessary attribute for the calculator object.

        Parameters
        ----------
        number: float
            an integer or floating digit set to 0 as default value
        """
        self.__number = 0

#shows current number
    @property
    def getNumber(self) -> float:
        """Returns the current value of calculator"""
        return self.__number

#resets current number to zero
    def reset(self) -> float:
        """Resets calculator's memory to 0"""
        self.__number = 0
        return self.__number

#adds a number
    def add(self, input: float) -> float:
        """Takes in a float input, returns the sum of input and number"""
        self.__number += input
        return self.__number

#subtracts a number
    def subtract(self, input: float) -> float:
        """Takes in a float input, returns the difference of number and input"""
        self.__number -= input
        return self.__number

#multiplies a number
    def multiply(self, input: float) -> float:
        """Takes in a float input, returns the product of number and input"""
        self.__number *= input
        return self.__number

#divides a number
    def divide(self, input: float) -> float:
        """Takes in a float input, returns the quotient of number and input"""
        self.__number /= input
        return self.__number

#takes nth root from a number
    def nroot(self, n: float) -> float:
        """Takes in a float n, returns the nth root of number"""
        self.__number **= 1.00/n
        return self.__number

