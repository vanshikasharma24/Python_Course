list1=[1,2,3,4,5,5,6,7,8]
for items in list1:
    print(items)
list2=[["vanshika","sharma"],["nandani","bhuria"],["pratima","patel"],["diksha","sadhuriya"]]
# print(list2)
# for name,surname in list2:
#     print(name,surname)
dict=dict(list2)
# print(dict)
for name, surname in dict.items():
    print(name,surname)