#Multiple Inheritance  
class A:
    def greet(self):
        print("In A")
class B:
   def greet(self):
        print("In B")
class C(A,B):
    pass
objC=C()
objC.greet()