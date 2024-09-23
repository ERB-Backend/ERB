# # Write a BMI calculator by user input
# # BMI formula : Weight (kg) / Height(m)^2
# #Hint:
#
# weight = float(input("Enter your weight"))
# height = float(input("Enter your height in cm: "))
# z = height **2
# print("square of z is", z**2)

words = "Today is a beautiful sunny day! Today is also Sunday!"
word = words.split()
count = dict()

for i in word:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1
print(word)
print(count)