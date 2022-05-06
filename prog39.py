#class variable and instance variable
class Employee:
    no_of_leaves=7#class variable
#class variable cant be changed by object it can be changed by class only
#class variable is shared by all the instances

harry=Employee()
rohan=Employee()

harry.std=9#instance variable
harry.salary=455
harry.role="instructor"
rohan.std=9
rohan.salary=4555
rohan.role="student"
print(harry.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves=9
harry.no_of_leaves=10
print(harry.no_of_leaves)#new variable for harry is created for 9 leaves 
print(Employee.no_of_leaves)