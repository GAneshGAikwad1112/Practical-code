class Employee:

    company = "Google"

    def __init__(self, name,  salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is Created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subnit of the employee is {self.subunit}")
harry = Employee('harry',100, "Youtube")
harry.getDetails() 