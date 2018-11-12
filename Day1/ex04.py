'''
module ex04

working with abstract classes and method
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    PI = 3.14

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius=1.0):
        self.__radius = radius
    
    def area(self):
        return self.PI * self.__radius ** 2

    # @property # -> this will act as a read only property
    # def area(self):
    #     return self.PI * self.__radius ** 2

def main():
    c1 = Circle(4.5)
    print ('Area of the circle', str(c1.area()))
    # print('Area of the circle', str(c1.area) # if we decorate the area fn. with property attribute
if __name__ == "__main__":
    main()