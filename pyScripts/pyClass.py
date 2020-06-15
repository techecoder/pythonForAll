# Class and Instantiation
import math


class Student:  # Define Class student
    a = 0  # This is class variable, hence no need to put self while calling outside class

    # __init__ funtion will always called whenever new object will be instantiated
    # Python will always pass one argument by default whenever init method is called within class
    def __init__(self, first, last):
        self.first = first  # Instance variables declaration, Always be called with self prefix outside class
        self.last = last
        self.mail = first + "." + last + "@xyz.com"

    def fullname(self):  # Any menthod called within class will have self argument by default
        print(Student.a)  # Class variables should be called with class prefix
        return '{} {}'.format(self.first, self.last)


# Object instantiated from Class student
s1 = Student('Tom', 'Harry')  # we can instantiated multiple objects from student class
s2 = Student('John', 'Snow')
s2.id = '1234'  # We can add new variable to s1 object which will only be limited to s1 only
print(s1.fullname(), s1.mail, )
print()
print(s2.fullname(), s2.mail, s2.id)
print()
print(Student.fullname(s1))  # another way to call object variables
print()
print(s1.__dict__)  # special attribute for object to show variables in dict form
print()
print(Student.__dict__)  # special attribute for class to show all details in dict form


# Class and inheritance subclass with getter and setter best practice
class Shape:
    def __init__(self, shape_type, color='Red'):  # Define the default method this class should execute
        self.__type = shape_type  # Instance variables
        self.__color = color

    def get_type(self):  # Getter method best practice
        return self.__type

    def get_color(self):
        return self.__color

    def get_area(self):  # Default method defined, which can be override in derived class or subclass
        pass

    def get_perimeter(self):  # Default method defined, which can be override in derived class or subclass
        pass


# Define a subclass and inherit Share class properties in it
class Square(Shape):
    def __init__(self, color, side):
        Shape.__init__(self, 'Square', color)
        self.__side = side

    def get_area(self):  # Derived Circle class defined get_area method calculation and override it
        return self.__side * self.__side

    def get_perimeter(self):  # Derived Circle class defined get_perimeter method calculation and override it
        return 4 * self.__side


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(self, 'Circle')  # Base class method variables can be called with super() as well
        self.__color = color
        self.__radius = radius

    def get_area(self):  # Derived Circle class defined get_area method calculation and override it
        return math.pi * self.__radius * self.__radius

    def get_perimeter(self):  # Derived Circle class defined get_perimeter method calculation and override it
        return 2 * math.pi * self.__radius


# Instantiation of subclasses Circle and Square
Circle1 = Circle('Green', 5)
Square1 = Square('Yellow', 5)
print(type(Circle1), type(Square1), Circle1.get_type(), Square1.get_type(), Square1.get_color(), Circle1.get_color())
print()
print(Circle1.get_area(), Circle1.get_perimeter(), Square1.get_perimeter(),
      Square1.get_area())  # Print area and perimeter by calling methods defined in subclass
print(issubclass(Square, Shape))  # TO check if Circle is derived class of Shape class or not


# Multiple Inheritance
class Father:
    def height(self):
        print("I have inherited Height from my Father")


class Mother:
    def intelligence(self):
        print("I have inherited intelligence from my Mother")


class child1(Father, Mother):  # Child subclass inherited from both Father and Mother class
    def experience(self):
        print("My experience are all my own")


c1 = child1()
c1.height()  # calling Base method
c1.intelligence()  # calling Base method
c1.experience()  # calling derived method