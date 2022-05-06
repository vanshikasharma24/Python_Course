import array as arr
a=arr.array('i',[1,2,3,4,5])
print(a[0])
#changing element
a[0]=10
print(a[0])
a[1:3]=arr.array('i',[22,45,18])
print(a)
#deleting element
del a[2]
print(a)
# concatination
arr1=arr.array('i',[2,6,3,8,5])
arr2=arr.array('i',[2,0,3,4,5])
arr3=arr.array('i')
arr3=arr1+arr2
print(arr3)