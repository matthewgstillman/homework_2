#Homework 4
#1. Write a program the rolls the dice 50 times and then tells you the number of times the dice lands on
#1, 2, 3, 4, 5 and 6
import random
one_count=0
two_count=0
three_count=0
four_count=0
five_count=0
six_count=0
# for loop starts
for i in range(1,51):
    roll_number = i
    number=random.randint(1,6)
    if number == 1:
        roll_number = i
        one_count += 1
        print("Roll Number {} - You rolled a {}. It is instance number {} of a {}".format(roll_number, number, one_count, number))
    elif number == 2:
        roll_number = i
        two_count += 1
        print("Roll Number {} - You rolled a {}. It is instance number {} of a {}".format(roll_number, number, one_count, number))
    elif number == 3:
        roll_number = i
        three_count += 1
        print("Roll Number {} - You rolled a {}. It is instance number {} of a {}".format(roll_number, number, one_count, number))
    elif number == 4:
        roll_number = i
        four_count += 1
        print("Roll Number {} - You rolled a {}. It is instance number {} of a {}".format(roll_number, number, one_count, number))
    elif number == 5:
        roll_number = i
        five_count += 1
        print("Roll Number {} - You rolled a {}. It is instance number {} of a {}".format(roll_number, number, one_count, number))
    elif number == 6:
        roll_number = i
        six_count += 1
        print("Roll Number {} - You rolled a {}. It is instance number {} of a {}".format(roll_number, number, one_count, number))
    else:
        print("Where the hell did you get that dice cube from?")

print("One Count: {}, Two Count: {}, Three Count: {}, Four Count: {}, Five Count: {}".format(one_count, two_count, three_count, four_count, five_count, six_count))
## End for loop
## Print out the number of times the dice lands on 1, 2, 3, 4, 5, 6


#2. Write a program that counts for the user. Let the user enter the starting number or the ending
#number, and the amount by which to count.
#For example,
#if the user enters 5 (starting number) and 4 (amount to count),
#the program outputs 5, 6, 7, 8
#If the user enters 6 (ending number) and 3 (amount to count),
#the program outputs 6, 5, 4
import random
print("User Counting Game")
starting_number = int(input("Enter a number to start counting from: "))
print("Starting Number: {}".format(starting_number))
counting_number = int(input("Enter a number of numbers to count to: "))
print("Counting Number: {}".format(counting_number))
increment = int(input("Enter a number count by incrementally: "))
print("Counting Increment: {}".format(increment))
for i in range(starting_number, counting_number, increment):
  print(str(i) + ",")


#3. BONUS
#Write a loop that asks for an integer from the user and then calculates the total of a series of number
#For example, if the number is 3. The series is 1/3 + 2/2 + 3/1
#If the number is 4, the series is 1/4 + 2/3 + 3/2 + 4/1
#The program should ask for the number again if the user enters a negative number or 0
#(Hint: While loop)
number_list = []
number_sum = 0.0
user_integer = int(input("Input an integer: "))
if user_integer <= 0:
    user_integer = int(input("Please Input a positive integer: "))
users = user_integer
i = 1
for i in range(1, users):
  while users > 0:
    print(str(i) + "/" + str(users))
    calculation = float(i/users)
    number_list.append(calculation)
    i += 1
    users -= 1
print("Number List: " + str(number_list))
for number in number_list:
  number_sum += number
print("Final Sum: {0:.2f}".format(number_sum))