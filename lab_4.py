#Lab 4
#1. Write a program that keeps a running total of the number of bugs collected for 5 days. The loop
#should ask for the number of bugs collected for each day. When the loop is finished, the program should
#display the total number of bugs collected.
number_of_days = 5
total_bugs = 0
for i in range(1, 6):
    print("Day {}".format(i))
    bugs_caught_today = input("How many bugs did you catch today?")
    total_bugs += int(bugs_caught_today)
    i += 1
average_bugs_caught = total_bugs / days
print("Total Bugs Caught: {}".format(total_bugs))
print("You caught an average of {} bugs per day!".format(average_bugs_caught))
#2. Please see an excerpt of code
###########################################################
# Enter a percentage between 0.0 to 5.0%
# For example, you can enter 2.5%
#<Please add your code here>
#<Please do not redefine bank balance or rate>
# HINT:
# 1. Use function strip() or replace() to get you the right format
# 2. Convert both balance and rate to the appropriate data type
# 3. Divide rate by 100
bank_balance="$250,000"
rate=input("What is the bank interest rate? (Enter a percentage between 0.0 to 5.0% - For example, you can enter 2.5%)")
rate_as_percentage = float(rate) / 100
formatted_bank_balance = bank_balance.strip("$")
final_formatted_bank_balance = formatted_bank_balance.replace(",", "")
print("Final Formatted Bank Balance: " + str(final_formatted_bank_balance))
float_bank_balance = float(final_formatted_bank_balance)
interest_earned = float_bank_balance * rate_as_percentage / 12
total_plus_interest = interest_earned + float(final_formatted_bank_balance) 
print("Interest Earned For this month is: ${0:.2f}".format(interest_earned))
print("Total Plus Interest: ${0:,.2f}".format(total_plus_interest))
###########################################################
#How do you print out online help for python build-in functions you don’t know? Try the help command