# myMax = lambda x, y: x if x > y else y
# print(myMax(2, 8))


myD = {"name": "Kelly",
"age": 25,
"job": "Accountant",
"university": "CU"}
myL = ['age', 'university']

newD={}

# for x in myL:
#     newD[x]=myD[x]

# for key in myL:
#     myD.pop(key)

for key in myD:
    if key not in myL:
        newD[key] = myD[key]

print(newD)

print(myD)