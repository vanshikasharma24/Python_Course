#different ways of formatting strings
#using %
import math
str1="vanshika"
a="hello my name is %s" %str1
print(a)
#by using tupple
str3="atharva"
age=15
b="hello my name is %s and my age is %d"%(str3,age)
print(b)
#using format
str="this is a {1}"+" "+"{0} module"
print(str.format("python","best"))
#f string
color="black"
food="kachori"
print(f"atharva fav color is{color}and his fav food is {food}{math.cos(45)}")