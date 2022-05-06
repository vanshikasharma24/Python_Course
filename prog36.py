#map filter and reduce
#"A map function executes certain instructions or functionality provided to it on every item of an iterable."
items=[2,3,4,5,6,7,8,9]
a=list(map((lambda x:x*x),items))
print(a)
#////////////////////////////////////////////
numbers=["5","6","7"]
a=list(map(int,numbers))
a[2]=a[2]+1
print(a[2])
##############################################
def square(a):
    return a*a

def cube(a):
    return a*a*a


func = [square, cube]
num = [2,3,5,6,76,3,3,2]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)

#"A filter function in Python tests a specific user-defined condition for a function and returns an
# iterable for the elements and values that satisfy the condition or, in other words, return true."
list1=[4,2,7,8,9,10]
a=list(filter((lambda x:x>5),list1))
print(a)
#"Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant"
from functools import reduce
list2=[2,3,4,9,1,5]
num = reduce(lambda x,y:x*y, list1)
print(num)