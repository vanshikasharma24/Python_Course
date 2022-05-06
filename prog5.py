#dictionary and its functions
d1={"vanshika":"sings","atharva":"plays","mom":"cooks","papa":"teaches"}
print(d1)

#accesing the elemets
print(d1["vanshika"])
print(d1["vanshika"],d1["atharva"])
#dictionary with in the dictinary
d2={"vanshika":"sings","atharva":"plays","mom":"cooks","papa":{"morning":"tea","afternoon":"works","night":"sleeps"}}
print(d2)
print(d2["papa"])
print(d2["papa"]["afternoon"])
#adding pairs to dictionary
d2["ankit"]="junk food"
print(d2)
d2.update({"leena":"dances"})
print(d2)
#del the pairs
del d2["leena"]
print(d2)
print(d2.keys())
print(d2.items())