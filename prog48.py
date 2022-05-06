#polymorphism through method overriding and variale overriding
#Overriding occurs when a derived class or child class has the same method that has already been defined in the base or parent class.
#variable overriding
class A:
    classvar1="i am a variable in class a"
    def __init__(self):
        self.var1="i am a A Constructor"
        self.classvar1="i am a instance var of class A"
        self.special="i am a special variable"
class B(A):
    classvar1="i am a variable in class B"
    def __init__(self):
        super().__init__()
        self.var1="i am a B Constructor"
        self.classvar1="i am a instance var of class B"
        # super().__init__()

a=A()
b=B()
#only overridden method will run with its object
#suppose i want to print the var or method of class a constructor i need to use super keyword
#IF WE TALK ABOUT THE VARIABLE THEN THE PRIORITY WILL BE FIRST GIVEN TO INSTANCE VARIABLE THEN TO CLASS VARIABLE
print(a.classvar1)
print(a.special)
print(b.var1)

