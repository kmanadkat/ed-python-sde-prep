class Employee:
    def __init__(self, ID=None, salary=0, department=None) -> None:
        self.ID = ID
        self.salary = salary
        self.department = department


Steve = Employee(128, 2500, 'Human Resource')
Mark = Employee()
print(Steve.__dict__)
print(Mark.__dict__)
