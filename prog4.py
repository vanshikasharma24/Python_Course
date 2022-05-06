#list
mylist=["1","2","8","4","5"]
print(mylist)
print(mylist[3])
yourlist=["2","hii"]
print(mylist+yourlist)
print(mylist[2:5:2])
print(mylist[-5:-1:2])
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
mylist.append(7)
print(mylist)
mylist.pop()
print(mylist)
mylist.insert(3,56)
print(mylist)
#tupple++
tup=(1,2,"van")
# tup[2]=4#immutable
# print(tup)
#swapping so easy
a= 1
b = 8
a, b = b,a
# temp = a
# a = b
# b = temp
print(a, b)