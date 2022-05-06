s = set()
print(type(s))
#its easy to make set from list
l=[1,2,3,4,5]
print(set(l))
#add
s2 = set()
s2.add(1)
s2.add(2)
print(s2)
s2.remove(1)
print(s2)
print(s.isdisjoint(s2))
print(s.union(s2))