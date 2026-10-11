# day - 1
# name = "Akshay"
# name2 = "tanya"

# print(name)
# print(name2)

# data types
# Number
# - Integer
# - Float
# - Complex

# Boolean

# Sequence type
# - String

# Data structure
# - List
# - Tuple
# - Set
# - Dictionary


# a = 12
# b = 12.67
# c = 6j
# print(a,b,c)

# is_logged_in = True
# print(is_logged_in)

# user = input("Enter your name: ")

# print("Your name:",user)

# operators
# operate number values
# connect add 
# Arithmetic 
# Assignment
# Comparisan
# Logical
# Identical and membership operator

# print(100%3)

# a = 10
# a/=3
# a = a % 3
# print(a)

# 0, "", [] , 76457367325646752 = true
# print(not((10<20 or 10>5) and 90 > 100))
# print(not 10)
# print(not {})
# and = all true then true
# or = any true then true
# not = if true then false (does opposite)


# a = 10
# b = 20
# result = not b<20 and a < b and b < 100 or False
# not -> and -> or
# print(result)

# [10, 10] = True

# [12,12,12,12,]
# [  ]
# [     ]
# 10
# 11
# a = [10]
# b = [10]
# print(a is b)
# print(a == b)

# 10 == 10
# is -> memory
# True

# string = 'This is my first class'
# print("s" in string)
# print("is" in string)

# conditional statements
# - condition if true false
# if 10>20: # What to do when condition is true
#     print("True hai ye toh")
# else: # When false
#     print("Ye to false hai")

# age = 32

# less than or equal 0 and greater than 150 then invalid age
# 1 - 12 kids
# 13 - 17 - Teen
# 18 - 60 - adult
# 61 < - You're ancient

# if (age <= 0 and age > 150):
#     print("Invalid age")
# elif (age > 0 and age <= 12):
#     print("Kids")


# a = "10"
# print(float(a)+10)

# Implicit -> simple 
# a = "10"
# a = 10
# a = 10
# b = 20
# c = b/a

# print(c)

# Explicit
# int() # -> float, str -> "char", "10" 
# str()
# float()
# bool()


# int(input("Enter :"))
# "19"
# "10.29"


# "a,b,c,d,e"
# print("a")
# print("b")


# while, for loops

# while -> condition stay true

# i = int(input("Enter: "))
# while i<100:
#     print("hello", i)
#     i += 1

# for -> number of times
# for x in range(start, stop(-1), step)

# for i in range(1, 101, 5):
#     print(i)

# for i in range(100, 0, -5):
#     print(i)

# user range start end
# start = int(input("Enter start: "))
# end = int(input("Enter end: "))

# for i in range(start, end+1, 1):
#     if not(i % 2 == 0):
#         print(i)

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# print("a", end="")
# print("b")

# for row in range(1, 6):
#     for col in range(1, 6):
#         print("*", end=" ")
#     print()

# * * * * *

# row = 1           col = 1
# row = 2           col = 2
# row = 3           col = 3
# row = 4           col = 4
# row = 5           col = 5
#   1 2 3 4 5
# 1 *
# 2 * *
# 3 * * *
# 4 * * * *
# 5 * * * * *


# for row in range(1, 6):
#     for col in range(1, row+1): # 
#         print("x", end=" ")
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *


# for row in range(1, 6):
#     for col in range(1, row+1): # 
#         print("*", end=" ")
#     print()
# for row in range(1, 5):
#     for col in range(4, row-1, -1):
#         print("*", end=" ")
#     print()

# - - - - *
# - - - * *
# - - * * *
# - * * * *
# * * * * *

# - - - -
# - - - 
# - - 
# - 


# for row in range(1, 6):
#     for space in range(5, row, -1):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()

# Homework (mandatory)

# * * * * *
# - * * * *
# - - * * *
# - - - * *
# - - - - *

# row = 1
# while row<6:
#     col = 1
#     while col<6:
#         print("*", end=" ")
#         col+=1
#     row+=1
#     print()

# break, continue, pass
# custom patterns
