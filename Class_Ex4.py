class Person:
    def __init__(self,name,age,address,c_no):
        self.name=name
        self.age=age
        self.address=address
        self.c_no=c_no
    def display(self):
        print(f"{self.name} - {self.age} - {self.address} - {self.c_no}")

class Employee(Person):
    def displayEmp(self):
        print(f"{self.name} in displayEmp")

obj=Person("Daksh",20,"C G Road",454545)
obj.display()
class Person:
    def __init__(self,name,age,address,c_no):
        self.name=name
        self.age=age
        self.address=address
        self.c_no=c_no
    def display(self):
        print(f"{self.name} - {self.age} - {self.address} - {self.c_no}")

obj=Person("Daksh",20,"C G Road",454545)
obj.display()

obj1=Employee("poiuy",34,"Parimal",45454545)
obj1.display()
obj1.displayEmp()