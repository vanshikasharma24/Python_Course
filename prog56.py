#comprehensions
#Using comprehension, we compress the code so it takes less space.
#list comprehension
# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
ls=[i for i in range(100) if i%3==0]
print(ls)
#dictionary cpmprehension
dict1= {i: f"item{i}" for i in range(1,8)}
print(dict1)
#reversing
dict2={ value:key for key,value in dict1.items()}
print(dict2)
#set comprehensions
dresses = {dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]}
print(type(dresses))
print(dresses)
#generator comprehensions
even = (i for i in range(100) if i%2==0)
print(even.__next__())
print(even.__next__())
print(even.__next__())
print(even.__next__())
print(even.__next__())
