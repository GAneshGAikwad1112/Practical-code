class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
harrysApplication = RailwayForm()
harrysApplication.name = "Harry"
harrysApplication.train = "abc express"
harrysApplication.printData()