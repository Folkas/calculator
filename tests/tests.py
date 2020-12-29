# importing pytest package
import pytest

class calculator:
    def __init__(self, number = 0) -> None:
        self.__number = 0

    @property
    def getNumber(self) -> float:
        return self.__number

    def reset(self) -> float:
      self.__number = 0
      return self.__number

    def add(self, input: float) -> float:
      self.__number += input
      return self.__number

    def subtract(self, input: float) -> float:
      self.__number -= input
      return self.__number

    def multiply(self, input: float) -> float:
      self.__number *= input
      return self.__number

    def divide(self, input: float) -> float:
      if input == 0:
          raise ZeroDivisionError
      self.__number /= input
      return self.__number

    def nroot(self, input: float) -> float:
      self.__number **= 1.00/input
      return self.__number

test1 = calculator()

#check if resets properly
def test_reset():
  assert test1.reset() == 0

#check if adds correctly
def test_add():
  assert test1.add(10) == 10

#check if subtracts correctly
def test_subtract():
  assert test1.subtract(6) == 4

#check if multiplies correctly
def test_multiply():
  assert test1.multiply(9) == 36

#check if divides correctly
def test_divide():
  assert test1.divide(2.25) == 16

#check if takes nth root correctly
def test_nroot():
  assert test1.nroot(4) == 2

#check if gets correct number
def test_getNumber():
  assert test1.getNumber == 2

#check if zero division works well
def test_zeroDivision():
    with pytest.raises(ZeroDivisionError):
        test1.divide(0)
