#Lab 8
#1. Use the randint function to generate 50 lines of random integers between -20 and 20. Write these
#numbers to a file called random_numbers.txt.
#random_numbers.txt
#-20
#-2
#0
#5
#...
#...
import random

fileh = open("random_numbers.txt","w")
# fileh.write(str(num))

for i in range(1,51):
    number = random.randint(-20,20)
    fileh.write(str(number))
    fileh.write(str(" "))

with open("random_numbers.txt") as fh: 
    lines = fh.readlines()
    for i in lines:
        words = i.split()
        print(words)

#2. Now append the file to add in the average of these 50 numbers
#random_numbers.txt
#-20
#-2
#...
#...
#The average of these 50 numbers is 0.28
#3. Exception
#x = float('abc123')
#What type of error does it raise? How would improve the error message that comes with the exception?
#4. Remember the Tipper program from lab 2. It asks users for the total bill amount and the program
#calculates the bill. What if the user enters a string? What exception will be raised. Please write a
#type/except handler to handle to exception
#Hint:
#try:
#...
#...
#except <Exception Type>:
#...
#...