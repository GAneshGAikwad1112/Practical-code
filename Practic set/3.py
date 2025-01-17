class Employee:
    salary = 10000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary* self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)

print(e.increment)
e.salaryAfterIncrement = 20000
print(e.salaryAfterIncrement)
print(e.increment)
