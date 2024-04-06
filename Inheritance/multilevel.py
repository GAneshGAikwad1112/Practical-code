class Person:
    country = "India"
    city = "Pune"
    def takeBreath(self):
        print("I am Breathing......")

class Employee(Person):
    company = "HOnda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am Employee so i am luckily Braeakthing.....")

class programmer(Employee):
    company = "fiverrr"

    def getSalary(self):
        print(f"No salary for programmer")

p = Person()
p.takeBreath()
#print(p.company)
e = Employee()
e.takeBreath()
print(e.company)
pr = programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)

