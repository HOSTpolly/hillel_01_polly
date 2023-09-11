# Following the SOLID acronym, they are:

# The Single Responsibility Principle
# The Open-Closed Principle
# The Liskov Substitution Principle
# The Interface Segregation Principle
# The Dependency Inversion Principle
from math import pi
from typing import Protocol


class CanCalculateArea(Protocol):
    def calculate_area(self)->float:
         ...
         
    def correct_shape(self)->float:
        ...


class Circle:
    def __init__(self,radius:int)->None:
        self.radius:int=radius
    def calculate_area(self)->float:
        return pi*self.radius**2
class Square:
    def __init__(self,side:int)->None:
        self.side:int=side
    def calculate_area(self)->float:
        return self.side**2
    
class Diamond:
    def __init__(self,a:int,b:int)->None:
        self.a=a
        self.b=b
    def calculate_area(self)->float:
        return self.a*self.b
        
def validate(shape: CanCalculateArea, max_limit:float)->CanCalculateArea:
    if shape.calculate_area()>max_limit:
        raise ValueError("the area is too big")
    return shape
    
    
class main():
    c1=Circle(radius=12)
    s2=Square(side=10)
    
    shape1= validate(c1,1222)
    shape2=validate(s2,1323)
    shape3=validate("Hello",1323)
    
    print(shape1)
    print(shape2)

def foo(a:int):
    pass

foo("asdaas")