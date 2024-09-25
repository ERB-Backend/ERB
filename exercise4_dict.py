# words = "Today is a beautiful sunny day! Today is also Sunday!"
# word = words.split()
# count = dict()
#
# for i in word:
#     if i not in count:
#         count[i]=1
#     else:
#         count[i]+=1
# print(word)
# print(count)

# test = {
#     "Car": 4,
#     "Bicycle": 2,
#     "Train": "many"
#         }




# for i in test:
#     print(i, "has", test[i], "wheels")

transport = {"mode": ["Car", "Bicycle", "Train"],
             "wheels": [4, 2, "many"]
             }

for mode, wheels in zip(transport["mode"], transport["wheels"]):
    # print(f"{mode} has {wheels} wheels")
    print (mode, "has", wheels, "wheels.")
