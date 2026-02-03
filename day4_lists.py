# Day 4: Lists and loops practice

#Q1: Create a list of 5 numbers and print all elements using a loop.
num = [34, 67, 89, 78, 56]
for numbers in num:
    print(numbers)
#Q2: Find and print the sum of all numbers in a list.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for numbers in num:
    total = total + numbers
print ("Sum: ", total)
#Q3: Create a list of names and print only names with length > 4.
names = ["Zainab", "Zain", "Ali", "Ahmed", "Saif"]
for name in names:
    if len(name) > 4:
        print(name)
#Q4: Take 5 numbers from user, store in a list, then print:
#the list
#maximum number
#minimum number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
numbers_list = [num1, num2, num3, num4, num5]
print(numbers_list)
print(max(numbers_list))
print(min(numbers_list))
#Q5 (Fun)
#Create a list of favorite foods and print:
#I love <food>
#for each item.
foods = ["Biryani", "Shawarma", "Kheer", "Burgers"]
for items in foods:
    print("I love", items)

