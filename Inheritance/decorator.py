class Employee:
    company = "Bharat Gas"
    Salary = 5000
    Salarybonus = 200
    
    @property
    def totalSalary (self):
        return self.Salary + self. Salarybonus
    
    @totalSalary.setter
    def totalSalary(self, val):
        self.Salarybonus = val - self.Salary

e = Employee()
print(e.totalSalary)

e.totalSalary = 58000
print(e.Salary)
print(e.Salarybonus)