"""
Class methods work with class variables and are accessible using the class name rather than its object. Since all class objects share the class variables, class methods are used to access and modify class variables.

Class methods are accessed using the class name and can be accessed without creating a class object.

Syntax
To declare a method as a class method, we use the decorator @classmethod. cls is used to refer to the class just like self is used to refer to the object of the class. You can use any other name instead of cls, but cls is used as per convention, and we will continue to use this convention in our course.

Note: Just like instance methods, all class methods have at least one argument, cls.
"""


class Employee:
    # Class Variables
    organization = 'Xebia'

    # Initializer
    def __init__(self, ID=None, salary=0, department=None) -> None:
        # Instance Variables
        self.ID = ID
        self.salary = salary
        self.department = department

    @classmethod
    def getOrganization(cls):
        return cls.organization

    # Instance Method
    def tax(self):
        return self.salary * 0.2

    # Instance Method
    def salaryPerDay(self):
        return self.salary / 30


Steve = Employee(128, 2500, 'Human Resource')
print(Steve.__dict__)
print(Employee.getOrganization())
print(Steve.tax())
print(Steve.salaryPerDay())
