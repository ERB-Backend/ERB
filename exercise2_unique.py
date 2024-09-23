list1 = [5, "Peter", "Jenny", 3, 5, "Jenny"]

# newList = set(list1)
newList=[]

# Method 1
for i in list1:
    if i not in newList:
        newList.append(i)

print(newList)

# Method 2
for i in list1:
    if i in newList:
        pass
    else:
        newList.append(i)

print(newList)


