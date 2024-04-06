class Employee:
    company = "Google"

    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greed():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9 AM in the morning")

harry = Employee()
harry.salary = 10000
harry.getSalary("Thanks!")

harry.greed()
harry.time()