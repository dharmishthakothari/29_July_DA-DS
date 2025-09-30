'''---> Person (name,age,address) , 
			---> Student (name,age,address ,marks,percentage)
			-->Employee (name,age,address,department,salary)
			--> display data of student
			--->use inheritance if required
			-->Use init to inilize object

		is a relationship Student is Person 
						 Employee is Person	'''

class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print(f"{self.name} - {self.age} - {self.address}")

#student is person / Person is super class student subclass
#Reusing person class in Student class / exteding Person into Student 
class Student(Person):
    def __init__(self, name, age, address,marks,percentage):
        super().__init__(name, age, address)
        self.marks=marks
        self.percetage=percentage
    def display(self):
        # super().display()
        print(f"{self.name} - {self.percetage} - {self.marks}")

monak=Student("Monank",20,"Parimal",230,90)
monak.display()