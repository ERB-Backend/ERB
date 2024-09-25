# myD = {"name": "Kelly",
# "age": 25,
# "job": "Accountant",
# "university": "CU"}
# myL = ['age', 'university']
# #
# #
# #
# # for x in myL:
# #     newD[x]=myD[x]
#
# for key in myL:
#     myD.pop(key)
#
# print(myD)

# Given 3 sets, check whether:
# fruitA is subset of fruitC?
# fruitB is subset of fruitC?

fruitA = {"apple", "mango"}
fruitB = {"orange", "mango"}
fruitC = {"apple", "mango",
"watermelon"}

# Method 1

def check_subset(setA, setB):
    if(setA.intersection(setB)) == setA:
        print("It is subset")
    else:
        print("It is not a subset")


# # Method 2
# def check_subset(setA, setB):
#     if setA.issubset(setB):
#         print("It is subset")
#     else:
#         print("It is not a subset")



check_subset(fruitA, fruitC)
check_subset(fruitB, fruitC)


