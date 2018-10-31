#Mini Project #1 (BONUS. Up to 3 points)
#Due: 10/11
#1. Your program needs to do the following:
# Inputs: a series of numbers
# The program then selects 2 numbers from the series and generate new numbers using the 4
#mathematical operations
# Outputs: All the new numbers it can generate using the 4 basic mathematical operations (+, -, x
#and /)
# Don’t forget about warning messages. What are the error conditions?
#o The numbers input from the users are not int or float
#o Users enter less than 2 numbers
#o etc
#o etc
#For example:
#Series of numbers = 1,2,3
# to select=2
#Let’s say the 2 numbers selected are 1 and 3
#The program returns the following:
#4 (Addition: 1+3)
#2 and -2 (Subtraction: 3-1, 1-3)
#3 (Multiplication: 1x3)
#3, 0.3333 (Division: 3/1 and 1/3)
import random
numbers_list = []
second_numbers_list = []
new_numbers_list = []
print("Mini Project")
first_number = input("Input your first number: ")
if type(first_number) == "int" or type(first_number) == "float":
  print("User Input Numbers Must Not Be Integers or Floats")
numbers_list.append(first_number)
second_number = input("Input your second number: ")
if type(second_number) == "int" or type(second_number) == "float":
  print("User Input Numbers Must Not Be Integers or Floats")
numbers_list.append(second_number)
third_number = input("Input your third number: ")
if type(third_number) == "int" or type(third_number) == "float":
  print("User Input Numbers Must Not Be Integers or Floats")
numbers_list.append(third_number)
fourth_number = input("Input your fourth number: ")
if type(fourth_number) == "int" or type(fourth_number) == "float":
  print("User Input Numbers Must Not Be Integers or Floats")
numbers_list.append(fourth_number)
fifth_number = input("Input your fifth number: ")
if type(fifth_number) == "int" or type(fifth_number) == "float":
  print("User Input Numbers Must Not Be Integers or Floats")
numbers_list.append(fifth_number)
print("1st Number: {}, 2nd Number: {}, 3rd Number: {}, 4th Number: {}, 5th Number: {}".format(first_number,second_number, third_number, fourth_number, fifth_number))
print("Numbers List: {}".format(numbers_list))
for i in range(0,2):
  random_number = random.choice(numbers_list)
  second_numbers_list.append(random_number)
  print("Random Number: {}".format(random_number))
  i += 1
print("Random Numbers: {}".format(second_numbers_list))
first = second_numbers_list[0]
print("First Number: {}".format(first))
second = second_numbers_list[1]
print("Second Number: {}".format(second))
addition = int(first) + int(second)
print("Addition: {} + {} = {}".format(first, second, addition))
new_numbers_list.append(addition)
subtraction_1 = int(first) - int(second)
subtraction_2 = int(second) - int(first)
print("Subtraction: {} - {} = {} , {} - {} = {}".format(first, second, subtraction_1, second, first, subtraction_2))
new_numbers_list.append(subtraction_1)
new_numbers_list.append(subtraction_2)
multiplication = int(first) * int(second)
print("Multiplication: {} * {} = {}".format(first, second, multiplication))
new_numbers_list.append(multiplication)
division_1 = int(first) / int(second)
division_2 = int(second) / int(first)
print("Division: {} / {} = {}, Division: {} / {} = {:.2f}".format(first, second, division_1, second, first, division_2)) 
new_numbers_list.append(division_1)
new_numbers_list.append(division_2)
print("New Numbers List: {}".format(new_numbers_list))