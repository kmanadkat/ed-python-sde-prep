class Employee:
    # Class Variables
    organization = 'Xebia'

    # Initializer
    def __init__(self, ID=None, salary=0, department=None) -> None:
        # Instance Variables
        self.ID = ID
        self.salary = salary
        self.department = department

    # Instance Method
    def tax(self):
        return self.salary * 0.2

    # Instance Method
    def salaryPerDay(self):
        return self.salary / 30


Steve = Employee(128, 2500, 'Human Resource')
print(Steve.__dict__, Steve.organization)
print(Steve.tax())
print(Steve.salaryPerDay())
