#Mini Project #2 (BONUS. Up to 3 points)
#Due Date: 10/25
#Your program should convert any decimal integer into a 16-bit binary number and a 4-bit hexadecimal
#numbers. To make it easier, lets assume it is only an integer. As a challenge, if you want, you can write
#one that takes in a floating point number as well.
#Any numbering system can be summarized by the following relationship:

#User to enter a number - an integer or floating point
#If user enters 45.425:
#integer = 45
#decimal = 0.425
#while div != 1:
#   Keep on dividing and save it back to div
#   Use % to keep track of the remainder each time.
#   I plan to use a string(Jack says use a list)
#   rem = integer % 2
#   make sure you are not overwriting remainder each iteration
#while dec_part != 0 or count < 16:
#   count += 1
#   save the integer part in a list

#Use a dictionary and mapping for hex number - 0000 = 0


binary_hex_decimal_dict = {
    0: {
        'binary': '0000',
        'hex': 0,
        'decimal': 0,
    },
    1: {
        'binary': '0001',
        'hex': 1,
        'decimal': 1,
    },
    2: {
        'binary': '0010',
        'hex': 2,
        'decimal': 2,
    },
    3: {
        'binary': '0011',
        'hex': 3,
        'decimal': 3,
    },
    4: {
        'binary': '0100',
        'hex': 4,
        'decimal': 4,
    },
    5: {
        'binary': '0101',
        'hex': 5,
        'decimal': 5,
    },
    6: {
        'binary': '0110',
        'hex': 6,
        'decimal': 6,
    },
    7: {
        'binary': '0111',
        'hex': 7,
        'decimal': 7,
    },
    8: {
        'binary': '1000',
        'hex': 8,
        'decimal': 8,
    },
    9: {
        'binary': '1001',
        'hex': 9,
        'decimal': 9,
    },
    10: {
        'binary': '1010',
        'hex': 'A',
        'decimal': 10,
    },
    11: {
        'binary': '1011',
        'hex': 'B',
        'decimal': 11,
    },
    12: {
        'binary': '1100',
        'hex': 'C',
        'decimal': 12,
    },
    13: {
        'binary': '1101',
        'hex': 'D',
        'decimal': 13,
    },
    14: {
        'binary': '1110',
        'hex': 'E',
        'decimal': 14,
    },
    15: {
        'binary': '1111',
        'hex': 'F',
        'decimal': 15,
    },
}

binary = ""
number = 0
digit_count = 0

user_number = int(input("Enter a number: "))
division = user_number // 2
remainder = user_number % 2
#while division != 1 division = remainder
if division != 1:
    print("Division: {}".format(division))
    print("Remainder: {}".format(remainder))
    binary += str(remainder)
    division = remainder
    print("Division NOW =: {}".format(division))
    print("Binary: {}".format(binary))
elif division == 1:
    binary += str(remainder)
    division = remainder 
    print("Binary: {}".format(binary))

# user_number = int(input("Please type in a number!"))
# print(user_number)

# if user_number % 2 == 0:
#   number = 0
#   remainder = user_number // 2
#   binary += str(number)
#   digit_count += 1
#   print("Remainder: {}".format(remainder))
#   while remainder > 0:
#     while remainder % 2 == 0 and digit_count < 4:
#       remainder = int(remainder) // 2
#       print("New Remainder: {}".format(remainder))
#       binary += str(remainder)
#       digit_count += 1
#       print("Binary: {}".format(binary))
#       remainder = remainder // 2
#       print("Remainder: {}".format(remainder))
#       if remainder >= 0 and digit_count < 4:
#         remainder = int(remainder) // 2
#         print("Remainder = {}".format(remainder))
#         binary += str(remainder)
#         digit_count += 1
#         print("Binary Digit Count: {}".format(digit_count))
# else:
#   number = 0
#   binary += str(number)
#   remainder = user_number // 2
#   print("Remainder: {}".format(remainder))

#   while remainder > 0:
#     while remainder % 2 == 0 and digit_count < 4:
#       remainder = int(remainder) // 2
#       print("New Remainder: {}".format(remainder))
#       binary += str(remainder)
#       digit_count += 1


#     print("Binary Number: {}".format(binary))



# if user_number % 2 == 0 :
#   number = 0
#   binary += str(number)
#   remainder = user_number // 2
#   print("Remainder: {}".format(remainder))
# else:
#   user_number = 1
#   binary += str(number)

# while user_number > 1:
#   number /=  2
#   print("User Number: {}".format(number))
#   if user_number % 2 == 0:
#     number = 0
#     binary += str(number)
#   else:
#     number = 1
#     binary += str(number)

# print("Binary Value of {} is {}".format(user_number, binary))

# div_no_remainder = 2 // user_number
# print("Div No Remainder: {}".format(div_no_remainder))
# div = 2 % user_number
# print("Div: {}".format(div))

# for i in range(0, 16):
#   if i == user_number:
#     print("Binary Number Value of {}: {}".format(i, binary_hex_decimal_dict[i]['binary']))

binary = ""

user_number = int(input("Please type in a number: "))

#Test Case: 4 - 0100
#4 /2 = 2; 4 % 2 == 0: Remainder = 0
division = user_number  // 2
print("Division: {}".format(division))
remainder = user_number % 2
print("Remainder: {}".format(remainder))
binary += str(remainder)
print("Binary: {}".format(binary))

if division != 1:
    division = remainder // 2
    print("Division: {}".format(division))
    print("Remainder: {}".format(remainder))
    binary += str(remainder)
    digit_count += 1
    print("Binary: {}".format(binary))
    remainder == division // 2
    print("Remainder: {}".format(remainder))

if division == 1:
    binary += str(division)
    user_number = 1
    division = user_number // 2
    if division == 1:
        binary += str(division)
        user_number = 1
        division = user_number // 2
    else:
        division = remainder // 2
        print("Division: {}".format(division))
        print("Remainder: {}".format(remainder))
        binary += str(remainder)
        digit_count += 1
        print("Binary: {}".format(binary))
        remainder == division // 2
        print("Remainder: {}".format(remainder))
