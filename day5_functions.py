#Q1: Create a function that prints your name.
def info(name):
    print("My name is", name)
info("Zainab")
#Q2: Create a function that takes two numbers and prints their sum.
def addition(a,b):
    return a + b
result = addition(5,10)
print(result)
#Q3: Create a function that returns the square of a number.
def square(a):
    return a**2
result = square(3)
print(result)
#Q4: Create a function that takes a list of numbers and returns their sum.
def find_sum(numbers):
    total = 0
    for num in numbers:
        total = total+num
    return total
my_list = ([2, 4, 5, 7, 8])
result = find_sum(my_list)
print("Sum:",result)
#Q5: Create a function that prints: You are doing great, <name> 💪
def message(name):
    print("You are doing great",name,"💪")
message("Zainab")