class Employee:
    company = "Google"

    def getSalary(self):
        print(f"salary for this employee working in {self.company} with {self.salary}")

emp1 = Employee()
emp1.salary = 10000
emp1.getSalary()
#Employee.getSalary(emp1)