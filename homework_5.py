#Homework 5
#1. Modify your program that prints out a rectangle from lab 4 to print out
#A left-aligned triangle
#%
#%%
#%%%
#%%%%
symbol = "%"
for i in range(1, 6):
  print(symbol * i)
#and This triangle
#%
# %%%
# %%%%%
#%%%%%%%
pattern = input("What pattern do you want to use?")
height = int(input("What is the height of the triangle?"))
for i in range(height):
      line = " " * (height-1-i) + pattern * (2*i + 1) + " " * (height-1-i)
  print(line)
#Hint: You don’t need to ask for the length or the width. You only need to ask for the height of
#the triangle
#2. The local DMV office has asked your help to store the answers for the 20 multiple choice
#questions in a list. Here are the answers:
#1. A 2. B 3. D 4. A 5. D 6. C 7. B 8. A 9. B 10. A
#11. C 12. D 13. B 14. B 15. B 16. C 17. C 18. C 19. A 20. B
#Your program should ask the users to enter his answers for the questions. Your program should give
#a final score. Each question is worth 5 points. Total point is 100.
#Hint: You might want to use strip() so the spaces would be stripped away. It is optional.
answers = ['A', 'B', 'D', 'A', 'D', 'C', 'B', 'A', 'B', 'A', 'C', 'D', 'B', 'B', 'B',
 'C', 'C', 'C', 'A', 'B']
user_answers = []
length = len(answers)
print("Length: {}".format(length))
possible_answers = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
lowercase_answers = ['a', 'b', 'c', 'd']

first = input("Question # 1: Enter an answer: A, B, C, or D")
if first not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif first in lowercase_answers:
  first = first.upper()
  user_answers.append(first)
else:
    user_answers.append(first)
print('First Answer: {}'.format(first))

second = input("Question # 2: Enter an answer: A, B, C, or D")
if second not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif second in lowercase_answers:
  second = second.upper()
  user_answers.append(second)
else:
    user_answers.append(second)
print('Second Answer: {}'.format(second))

third = input("Question # 3: Enter an answer: A, B, C, or D")
if third not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif third in lowercase_answers:
  third = third.upper()
  user_answers.append(third)
else:
    user_answers.append(third)
print('Third Answer: {}'.format(third))

fourth = input("Question # 4: Enter an answer: A, B, C, or D")
if fourth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif fourth in lowercase_answers:
  fourth = fourth.upper()
  user_answers.append(fourth)
else:
    user_answers.append(fourth)
print('First Answer: {}'.format(fourth))

fifth = input("Question # 5: Enter an answer: A, B, C, or D")
if fifth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif fifth in lowercase_answers:
  fifth = fifth.upper()
  user_answers.append(fifth)
else:
    user_answers.append(fifth)
print('Fifth Answer: {}'.format(fifth))

sixth = input("Question # 6: Enter an answer: A, B, C, or D")
if sixth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif sixth in lowercase_answers:
  sixth = sixth.upper()
  user_answers.append(sixth)
else:
    user_answers.append(sixth)
print('Sixth Answer: {}'.format(sixth))

seventh = input("Question # 7: Enter an answer: A, B, C, or D")
if seventh not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif seventh in lowercase_answers:
  seventh = seventh.upper()
  user_answers.append(seventh)
else:
    user_answers.append(seventh)
print('Seventh Answer: {}'.format(seventh))

eigth = input("Question # 8: Enter an answer: A, B, C, or D")
if eigth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif eigth in lowercase_answers:
  eigth = eigth.upper()
  user_answers.append(eigth)
else:
    user_answers.append(eigth)
print('Eigth Answer: {}'.format(eigth))

ninth = input("Question # 9: Enter an answer: A, B, C, or D")
if ninth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif ninth in lowercase_answers:
  ninth = ninth.upper()
  user_answers.append(ninth)
else:
    user_answers.append(ninth)
print('Ninth Answer: {}'.format(ninth))

tenth = input("Question # 10: Enter an answer: A, B, C, or D")
if tenth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif tenth in lowercase_answers:
  tenth = tenth.upper()
  user_answers.append(tenth)
else:
    user_answers.append(tenth)
print('Tenth Answer: {}'.format(tenth))

eleventh = input("Question # 11: Enter an answer: A, B, C, or D")
if eleventh not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif eleventh in lowercase_answers:
  eleventh = eleventh.upper()
  user_answers.append(eleventh)
else:
    user_answers.append(eleventh)
print('Eleventh Answer: {}'.format(eleventh))

tweflth = input("Question # 12: Enter an answer: A, B, C, or D")
if tweflth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif tweflth in lowercase_answers:
  tweflth = tweflth.upper()
  user_answers.append(tweflth)
else:
    user_answers.append(tweflth)
print('Tweflth Answer: {}'.format(tweflth))

thirteenth = input("Question # 13: Enter an answer: A, B, C, or D")
if thirteenth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif thirteenth in lowercase_answers:
  thirteenth = thirteenth.upper()
  user_answers.append(thirteenth)
else:
    user_answers.append(thirteenth)
print('Thirteenth Answer: {}'.format(thirteenth))

fourteenth = input("Question # 14: Enter an answer: A, B, C, or D")
if fourteenth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif fourteenth in lowercase_answers:
  fourteenth = fourteenth.upper()
  user_answers.append(fourteenth)
else:
    user_answers.append(fourteenth)
print('Fourteenth Answer: {}'.format(fourteenth))

fifteenth = input("Question # 15: Enter an answer: A, B, C, or D")
if fifteenth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif fifteenth in lowercase_answers:
  fifteenth = fourteenth.upper()
  user_answers.append(fifteenth)
else:
    user_answers.append(fifteenth)
print('Fifteenth Answer: {}'.format(fifteenth))

sixteenth = input("Question # 16: Enter an answer: A, B, C, or D")
if sixteenth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif sixteenth in lowercase_answers:
  sixteenth = sixteenth.upper()
  user_answers.append(sixteenth)
else:
    user_answers.append(sixteenth)
print('Sixteenth Answer: {}'.format(sixteenth))

seventeenth = input("Question # 17: Enter an answer: A, B, C, or D")
if seventeenth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif seventeenth in lowercase_answers:
  seventeenth = seventeenth.upper()
  user_answers.append(seventeenth)
else:
    user_answers.append(seventeenth)
print('Seventeenth Answer: {}'.format(seventeenth))

eighteenth = input("Question # 18: Enter an answer: A, B, C, or D")
if eighteenth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif eighteenth in lowercase_answers:
  eighteenth = eighteenth.upper()
  user_answers.append(eighteenth)
else:
    user_answers.append(eighteenth)
print('Eighteenth Answer: {}'.format(eighteenth))

nineteenth = input("Question # 19: Enter an answer: A, B, C, or D")
if nineteenth not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif nineteenth in lowercase_answers:
  nineteenth = nineteenth.upper()
  user_answers.append(nineteenth)
else:
    user_answers.append(nineteenth)
print('Nineteenth Answer: {}'.format(nineteenth))

twentieith = input("Question # 20: Enter an answer: A, B, C, or D")
if twentieith not in possible_answers:
    print("Error! Not a Properly Formatted Answer!")
elif twentieith in lowercase_answers:
  twentieith = twentieith.upper()
  user_answers.append(twentieith)
else:
    user_answers.append(twentieith)
print('Twentieith Answer: {}'.format(twentieith))

print("User Answers: {}".format(user_answers))

user_right_count = 0
user_wrong_count = 0

for i in range(0, len(user_answers)):
    if user_answers[i] == answers[i]:
        user_right_wrong.append("Right")
        user_right_count += 1
    else:
        user_right_wrong.append("Wrong")
        user_wrong_count += 1

user_correct_percentage = 100 * (float(user_right_count) / float(length))

print("You got {} correct answers out of {} questions. Your final score is {}%".format(user_right_count, length, user_correct_percentage))
print("User Right Wrong: {}".format(user_right_wrong))


#3.Try these following commands
mystr="Happy Birthday to you and your friends"
print(mystr[::-1])
print(mystr[0:2])
print(mystr[10:30])
print(mystr[30:10:-1])
print(mystr[30:10:-2])
#Do you know why these commands do? Do you understand the output?mystr="Happy Birthday to you and your friends!"
mystr="Happy Birthday to you and your friends"
print(mystr[::-1])
#Output: sdneirf ruoy dna uoy ot yadhtriB yppaH
# prints the entire list in backwards oreder
print(mystr[0:2])
#Output: Ha
# - prints the first two characters
print(mystr[10:30])
#Output: hday to you and your
# - Prints indexes 10 through 29
print(mystr[30:10:-1])
#Output: ruoy dna uoy ot yad
# - Prints indexes 30 through 11
print(mystr[30:10:-2])
#Output: uydauyo a
# - Prints backwards every other index from 30 to 11 
#Do you know why these commands do? Do you understand the output?
