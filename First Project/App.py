# print("I am Zanga")
# print('o----')
# print(' ||||')
# print('*' * 10)
#
# patient_fullname = 'Silicon'
# patient_age = 20
# is_new = True
from operator import truediv

# name = input('What is your name? ')
# colour = input('what is your favourite color? ')
# print(name + ' likes ' + colour)

# birth_year = input('Birth Year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# user_weight = input('Weight (lbs): ')
# kilogram = int(user_weight) * 0.4536
# print(kilogram)

# course = '''
# Hi John,
# Here's a testing email
# Thanks
# '''
# print(course)

# course = 'Testing index numbers'
# print(course[0])
# print(course[-1])
# print(course[0:3)
# name = 'Jennifer'
# print(name[1:-1])

# course = 'Python for Beginners'
# another = course[:]
# print(another)


# formatted strings

# first = 'John'
# last = 'Smith'
# message = f'{first} {last} is a coder'
# print(message)

# String Length
# name = 'Odusote is a man'
# print(len(name)) count number of characters
# print(name.upper()) uppercase
# print(name.lower()) lowercase
# print(name.replace('is a man', 'is a Professor'))
# print(name.replace('Odusote', 'Adekunle'))

# Boolean
# name = 'Oreoluwa is a girl'
# print('girl' in name)
# print('boy' in name)

# Arithmetic Operations
# print(10 * 3)
# x = 10 + 3 * 2 ** 2
# print(x)
# exponentiation 2 ** 3
# multiplication or division
# addition or subtraction

# Math Function
# x = 2.9
# print(round(x))
# print(abs(-2.9)) // Always returns a positive number

# If Statements
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a Lovely day")
#
# print('Enjoy your day')

# Exercise
# good_credit = True
# bad_credit = False
#
# if good_credit:
#     print("Pay 10%")
# elif bad_credit:
#     print("Pay 20%")
# else:
#     print("Pay the down payment")

# # Solution
# price = 1000000
# has_good_credit = False
#
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down Payment is: ${down_payment}")


# # has_high_income = False
# has_good_credit = True
# has_criminal_record = False
#
# # if has_high_income and has_good_credit:
# #     print("Eligible for Loan")
#
# # if has_high_income or has_good_credit:
# #     print("Eligible for Loan")
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for Loan")
#
# # AND: both condition should be true
# # OR: at least one should be true
# # NOT: one condition should be false

# name = "Rid"
#
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good!")


# # while loop
# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
# print("Done")
#
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done")


# # For Loop
# for item in 'Python':
#     print(item)
#
# for name in ['Mack, Rid, John, Bims']:
#     print(name)
#
# for item in range(10):
#     print(item)
#
#
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")


# # # Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

#
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     print('x' * x_count)
#
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)


# ## List
# names = ['John', 'Ridwan', 'Dare', 'Seun']
# names[0] = 'Jon'
# print(names[1:2])
# print(names[2])
# print(names)
#
# numbers = [3, 6, 2, 8, 4, 20]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


## Dimensional List (2D)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# matrix[0][1] = 20
# print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
