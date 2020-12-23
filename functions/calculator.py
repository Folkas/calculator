class calculator:
    def __init__(self, number = 0) -> None:
        self.__number = 0

#shows current number
    @property
    def getNumber(self) -> float:
        return self.__number

#resets current number to zero    
    def reset(self) -> float:
      self.__number = 0
      return self.__number

#adds a number
    def add(self, input: float) -> float:
      self.__number += input
      return self.__number

#subtracts a number
    def subtract(self, input: float) -> float:
      self.__number -= input
      return self.__number

#multiplies a number
    def multiply(self, input: float) -> float:
      self.__number *= input
      return self.__number

#divides a number
    def divide(self, input: float) -> float:
      self.__number /= input
      return self.__number

#takes nth root from a number
    def nroot(self, input: float) -> float:
      self.__number **= 1.00/input
      return self.__number
