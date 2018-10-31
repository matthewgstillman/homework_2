#Homework 3
#True or False
#1. You need to declare a variable before using it in Python
#False
#2. The input() function always return a value of type “string”
#False. The input function will return a float if you write this: float(input="What is your grade in Python class?"). It can return strings and integers as well.
#Short questions:
#1. Both randint and randrange are random number generators, but the syntax is slightly different.
#Please tell how you would generate a positive integer from 1 to 6
import random
print(random.randint(1,7))
#2. How do you use one of the string methods to change the string from “I love dogs” to “I don’t like
#dogs”? HINT: Use the function replace()
i_love_dogs = "I love dogs"
print("How do I feel about dogs?\n" + str(i_love_dogs))
i_dont_like_dogs = i_love_dogs.replace("love", "don't like")
print("How do I feel about dogs?\n" + str(i_dont_like_dogs))
#3. How would you use python to help you find the answers to the following questions
# 40 – 4a
# -------------- , where a =0.5 and b is 2
# 30 + 4b
a = 0.5
b = 2
calculation = (40 - (4 * a))/(30 + (4 *b))
print("Calculation = " + str(calculation))
#Output: Calculation = 1.0
#Programs
#1. Ask the user to input an integer. If it is even, print out “The number <user’s number> is an even
#number”. Otherwise, print out “The number <user’s number> is an odd number”. If the user does
#not input an integer, please print out “You didn’t enter an integer” Hint: Use isdigit() or isnumeric()
user_integer = int(input("Please Input an integer: "))
print("User Integer: " + str(user_integer))
if user_integer % 2 == 0:
  print("The number <user's number> is an even number")
elif user_integer % 2 != 0:
    print("The number <user's number> is an odd number")
else:
  if user_integer.isnumeric() == False:
    print("You didn't enter an integer")
#2. Money counting game. Ask the user to input the exact number of coins required to make exactly
#one dollar. The program should prompt the user to enter the number of pennies, nickels, dimes and
#quarters. If the total is exactly $1, the program congratulate the user. Otherwise, the program
#should display a message saying the total amount is x and it is more than or less than 1 dollar.
pennies = int(input("How many pennies?"))
penny_total = int(pennies) * 1
nickels = int(input("How many nickels?"))
nickel_total = int(nickels) * 5
dimes = int(input("How many dimes?"))
dime_total = int(dimes) * 10
quarters = int(input("How many quarters?"))
quarter_total = int(quarters) * 25
total = penny_total + nickel_total + dime_total + quarter_total
print("Total: " + str(total) + " cents")
if total < 100:
  short_money = 100 - total
  print("You are " + str(short_money) + " cents short of a dollar")
elif total == 100 :
  print("You have exactly one dollar. Congratulations")
if total > 100:
  print("You have more than a dollar. Congrats on that.")
