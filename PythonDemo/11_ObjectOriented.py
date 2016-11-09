# coding=utf-8


# Class Create
class Employee:
    'the base class of all employee'
    emp_count = 0


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1


    def display_count(self):
        print "Total Employee %d" % Employee.emp_count


    def display_employee(self):
        print "Name: %s, Salary: %d" % (self.name, self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.display_employee()  # Name: Zara, Salary: 2000
emp2.display_employee()  # Name: Manni, Salary: 5000
print "Total Employee %d" % Employee.emp_count  # Total Employee 2

emp1.age = 7
print hasattr(emp1, 'age')  # True
print getattr(emp1, 'age')  # 7

setattr(emp1, 'age', 8)
delattr(emp1, 'age')


# Class Build-in Fields
print "Employee.__doc__:", Employee.__doc__  # Employee.__doc__: the base class of all employee
print "Employee.__name__:", Employee.__name__  # Employee.__name__: Employee
print "Employee.__module__:", Employee.__module__  # Employee.__module__: __main__
print "Employee.__bases__:", Employee.__bases__  # Employee.__bases__: ()
print "Employee.__dict__:", Employee.__dict__  # Employee.__dict__: {'__module__': '__main__', 'emp_count': 2, 'display_employee': <function display_employee at 0x1072eede8>, 'display_count': <function display_count at 0x1072132a8>, '__doc__': 'the base class of all employee', '__init__': <function __init__ at 0x1072130c8>}


# Class Object Destory
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destory"


pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)  # 4565544616 4565544616 4565544616

del pt1
print "after call del pt1"
del pt2
print "after call del pt2"
del pt3
print "after call del pt3"
'''
after call del pt1
after call del pt2
Point destory
after call del pt3
'''


# Class Inheritance
class Parent:
    parent_attr = 100


    def __init__(self):
        print "call parent class init method"


    def parent_method(self):
        print "call parent class method"


    def some_method(self):
        print "call some method in parent class"


    def set_attr(self, attr):
        Parent.parent_attr = attr


    def get_attr(self):
        print "parent class attr:", Parent.parent_attr


class Child(Parent):
    def __init__(self):
        print "call child class init method"


    def child_method(self):
        print "call child class method"


    def some_method(self):
        print "call some method in child class"


c = Child()  # call child class init method
c.child_method()  # call child class method
c.parent_method()  # call parent class method
c.set_attr(200)
c.get_attr()  # parent class attr: 200
c.some_method()  # call some method in child class


# Class Operator Overload
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __str__(self):
        return "Vector (%d, %d)" % (self.a, self.b)


    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2  # Vector (7, 8)


# Class Field & Method
class JustCounter:
    __secret_count = 0
    public_count = 0


    def count(self):
        self.__secret_count += 1
        self.public_count += 1
        print self.__secret_count


counter = JustCounter()
counter.count()  # 1
counter.count()  # 2
print counter.public_count  # 2

try:
    print counter.__secret_count
except AttributeError, e:
    print e  # JustCounter instance has no attribute '__secret_count'

print counter._JustCounter__secret_count  # 2
