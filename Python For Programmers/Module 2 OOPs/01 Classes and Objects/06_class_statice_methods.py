"""
Static methods are methods that are usually limited to class only and not their objects. They have no direct relation to class variables or instance variables. They are used as utility functions inside the class or when we do not want the inherited classes to modify a method definition.

Static methods can be accessed using the class name or the object name.

Syntax
To declare a method as a static method, we use the decorator @staticmethod. It does not use a reference to the object or class, so we do not have to use self or cls. We can pass as many arguments as we want and use this method to perform any function without interfering with the instance or class variables.

Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes. The purpose of a static method is to use its parameters and produce a useful result.
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

    @staticmethod
    def printCard(ID, name):
        return f"Employee Code: {ID}\nEmploee Name: {name}"

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

print(Employee.printCard(Steve.ID, "Steve"))
