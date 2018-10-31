#Lab 5
#1. Consider the following program
# pattern = "*"
#What is printed out using the following commands?
# print("pattern ")
#Output: pattern 
# print(pattern)
#Output: *
# print(pattern+pattern)
#Output: **
# print(pattern*3)
#Output: ***
#2. Now using what you learned in step 1, please write a program that prints out a rectangle
# The program needs to ask the width and length of the rectangle as well as the pattern to use
#Hint:
print("Rectangle Program")
length = int(input("What length do you want your rectangle to be?"))
print("Length: {}".format(length))
width = int(input("What width do you want your rectangle to be?"))
print("Width: {}".format(width))
pattern = input("What do you want the pattern to be for your rectangle?")
print("Pattern: {}".format(pattern))
if length > width:
 for i in range(0, width):
     print(pattern * length)
elif length < width:
 for i in range(0, length):
   print(pattern * width)
else:
 print("The Length and With you entered, {} & {}, are equal. Your shape is a square - not a rectangle!")
#length=int(input("What is the length of your rectangle "))
#width=int(input("What is the width of your rectangle? "))
#pattern=input("What pattern do you want to use ")
# Use a for loop
#For example, if the user enters 5 for the length, 3 for the width and % as the pattern, the program
#outputs
#%%%%%
#%%%%%
#%%%%%
#3. Given the following employee database,
employees = [("John", 49, 120000), ("Patrick", 24, 80000), ("Olivia",38,150000)]
#Each tuple should be interpreted this way as (name, age, income)
#For example, John is 49 years old. He makes $120,000 a year in the company.
#Please try the following commands
#print (len(employees))
#Output: 3
#print(employees)
#Output: [("John", 49, 120000), ("Patrick", 24, 80000), ("Olivia",38,150000)]
#print(employees[1])
#Output: ('Patrick', 24, 80000)
#print (type(employees[1]))
#Output: <class 'tuple'>
#print(employees[1][0])
#Output: Patrick
#Now write a program to extract the names of the employees from the database. Your program should
#also print out the number of employees in the company
#Sample Output:
#There are 3 employees in the company. Their names are John, Patrick and Olivia.

employee_count = 0
names_list = []
j = 0
for i in range(0, len(employees)):
  name = employees[i][0]
  names_list.append(name)
  employee_count += 1
print("Names List: {}".format(names_list))

print("There are {} employees in the company. Their names are {}, {} and {}".format(employee_count, names_list[0], names_list[1], names_list[2]))


