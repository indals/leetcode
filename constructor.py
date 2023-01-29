class Employee:
    increment = 2.5
    def __init__(self,NAME,SALARY):
        self.name = NAME
        self.salary=SALARY
        self.increment=2
    

    def increase(self):
        self.salary = int(self.salary*Employee.increment)


suraj=Employee('suraj',40000)  
suraj.increase() 
print(suraj.__dict__)
print(Employee.__dict__)
print(suraj.salary)


