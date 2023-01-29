class Employee:
    increment = 1
    def __init__(self,Name, Salary):
        self.name = Name
        self.salary = Salary
    def increase(self):
        self.salary = int(self.salary*self.increment)
    
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount


saroj = Employee('saroj',5000)
Employee.change_increment(2)
print(saroj.increment)
saroj.increase()
print(saroj.salary)