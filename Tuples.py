#Tuple is immutable
tup=(1,2,76,32,"green",True)
#tup[0]=90
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
#print[34]
if "green" in tup:
    print("Yes! 342 is present in this tuple")
tup2=tup[1:4]
print(tup2)
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2])