#string slicing and other num
str="amazing"
print(str[0:6:2])
#by default first index is taken as 0 second index is taken as length of the whole string and last index is taken as 1
print(str[0:])
print(str[:4])
print(str[::])
print(str[-6:-1:2])
demo="i AM a good girl"
print(demo.find("good"))
print(demo.endswith("good"))
print(demo.count("o"))
print(demo.capitalize())
print(demo.upper())
print(demo.lower())
print(demo.replace("good","bad"))