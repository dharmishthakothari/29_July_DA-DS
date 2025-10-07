class Person:
    def __init__(self,name,address,salary):
        self.name=name
        self._address=address
        self.__salary=salary
    def display(self):
        print(f"{self.name} - {self._address} - {self.__salary}")
    def getSalary(self):
        return self.__salary
    def setSalary(self,salary):
        if salary<=0:
            return None
        else:
            self.__salary=salary
class Employee(Person):

    pass    
class Manager:
    pass
p=Person("test","parimal",2343434)
p.display()
e=Employee("test","Primal",343434)
print(f"{e.name} - {e._address} ")
e.setSalary(90000)
print(f"{e.getSalary()}")
e.display()
        
