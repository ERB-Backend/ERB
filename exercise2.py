list1 = [5, "Peter", "Jenny", 3, 5, "Jenny"]

# newList = set(list1)
newList=[]

for i in list1:
    if i not in newList:
        newList.append(i)

print(newList)