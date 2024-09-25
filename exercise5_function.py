# Write a BMI calculator by user input
# BMI formula : Weight (kg) / Height(m)^2
#Hint:

# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in cm: "))
#
# def BMI_calculator(weight, height):
#     converted_height_cm = (height/100)
#     bmi = weight/(converted_height_cm**2)
#     return bmi
# print(BMI_calculator(weight,height))

# input a length, calculate the volume of a cube

# length = float(input("Enter the length: "))
# def volume_calculator(length):
#     return length * length * length
#
# print(volume_calculator(length))

# Given a list of numbers [2, 4, 6]  Calculate the sum of square of these numbers. (i.e. 56)


# def volume_calculator(*numbers):
#     total = 0
#     for number in numbers:
#         total += number**2
#     return  total
#
# print(volume_calculator(2,4,6))


#Input a number and reverse showing the number. e.g. Input a number: 51342 return 24315
# num = input("Enter the number: ")
# def reverse(number):
#     new_num = int(number[::-1])
#     return new_num
#
# print(reverse(num))


#  Input 2 numbers (1st < 2nd) and find all prime numbers between these 2 numbers. Input 1st number: 11  Input 2nd number: 18# 11,13,15,17,

first = int(input("input first number"))
second = int(input("input second number"))

# Negative numbers, 0 and 1 are not primes



def cal_prime(num):
    if num > 1:

        # Iterate from 2 to n // 2
        for i in range(2, (num // 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                break
        else:
            print(num)

while second >= first:
    cal_prime(second)
    second -=1
