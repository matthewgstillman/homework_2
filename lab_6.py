#Lab 6
#1. Write a function called Greetings that prints out a greeting
#Note:
# The random greeting must include the person’s name. The default name is Doc
# You can have a list of greetings and randomly pick one to print
#Greetings()
#How are you, Doc?
#Good to see you. Have a good day
#Greetings(John)
#How are you, John?
#Nice to meet you. Have a nice day
import random
greetings_list = ['How are you, Doc?', 'Good to see you. Have a good day', 'Greetings(John)', 'How are you, John?', 'Nice to meet you. Have a nice day']
def greetings(name, greetings):
    random_greeting = random.choice(greetings)
    print("Hello, {}! {}".format(name, random_greeting))
    return

greetings("Matt", greetings_list)

#2. Write a program that accepts a LIST of numbers and returns the tuple (mean, median)
#Sample output:
#MeanMedian([1,2,9])
#(4,2)
import statistics 
number_list = [1,2,9]
def mean_median(numbers):
  number_list = [1,2,9]
  number_sum = 0
  length = len(number_list)
  print("Length: {}".format(length))
  print(number_sum)
  for i in range(0, len(number_list)):
    number_sum += number_list[i]
    print("sum = {}".format(number_sum))

  print("Final Sum = {}".format(number_sum))
  mean = number_sum / len(number_list)
  print("Arithmetic Mean: {}".format(mean))
  median_number = statistics.median(number_list)
  print("Median: {}".format(median_number))
  final_tuple = (mean, median)
  return(final_tuple)    

mean_median(number_list)

#3. Write a function call Fahrenheit to return the Fahrenheit equivalent ofa Celsius temperature.
#Then use this function that prints a chart showing the Fahrenheit equivalents (up to 1 decimal place) of
#all Celsius temperatures 0--40 degrees (There should be 41 lines)
#F = (9 / 5) * C + 32

def celsius_to_fahrenheit(c_degrees):
    fahrenheit = (9/5 * c_degrees) + 32
    print("{} Degrees Celsius Converts to {} Degrees Fahrenheit".format(c_degrees, fahrenheit))
    return("Counting Up...")

celsius_to_fahrenheit(0)

#Sample output:
#Celsius Fahrenheit
#0C 32F
#1C 33.8F
#…
# …
for i in range(0,41):
  print(celsius_to_fahrenheit(i))