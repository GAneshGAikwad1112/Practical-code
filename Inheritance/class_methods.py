class Employee:
    company = "Camel"
    salary = 100
    location = "Pune"

    @classmethod    #----------------class method related to class---------------------
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)