#abstract base class and abstract method
#abstract base class is used when we want to implement any function compulsorily on the child classes
#abc is a module in python class and abc meta is a python class which can give instruction to the child classes
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(Shape):
    type="rectangle"
    def __init__(self):
        self.length=6
        self.breadth=7
    def printarea(self):
        print("area is",self.length*self.breadth)
rec1=Rectangle()
sh1=Shape#cant make object of abstract class directly