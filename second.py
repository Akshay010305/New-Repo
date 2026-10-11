# day 2
# Guess the number
# guess = 12
# count = 0
# user = ""
# totalAttempts = 3
# Total 3 attempt 1 rest 2
# print("Total attempts available:", totalAttempts)
# print("-------------------------------------------")
# while (user!=guess) and (count!=3):
#     user = int(input("Enter your guess: "))
#     count+=1
#     print("-------------------------------------------")
#     print("Attempts taken:", count)
#     print("Remaining attempts:", totalAttempts-count)
#     print("-------------------------------------------")
    
#     if user == guess:
#         print("You have finally guessed it right!!", count)
#     elif (count == 3):
#         print("You have lost all chances.")
#     elif user > guess:
#         print("Your number is big")
#     elif user < guess:
#         print("Your number is smaller")

# while True:
#     user = int(input("Enter your guess: "))
#     count+=1
#     if user == guess:
#         print("You have finally guessed it right!!", count)
#         break
#     elif (count == 3):
#         print("You have lost all chances.")
#         break
    
# break -> ends loop
# continue -> skip an iteration
# pass -> does nothing

# i = 0

# while i<10:
#     if i==5:
#         continue
#     print(i)
#     i+=1

# for i in range(1, 11):
#     if i == 5:
#         pass
#     print(i)

# * * * * *
# *       *
# *       *
# * * * * *
# *       *
# *       *

# for row in range(1, 8):
#     for col in range(1, 6):
#         # print("Row:",row, "Col:", col, end=" |")
#         if (col==1 and row>=2) or (row==1 and (col>=2 and col < 5)) or (col==5 and (row!=1 and row!=4 and row!=7)) or (row==4 and (col>=1 and col<5)) or (row==7 and col<5):
#             print("*", end=" ")

#         else:
#             print(" ", end=" ")
#     print()
    
# name = "Akshay"    
# print(f"{name}")
# f-string


# Strings

# string sequence of characters
# enclose quotes '' "" '''''' """"""

# print("Hello") # For single line
# print('Hello') # For single line
# print('''H
# e
# l
# l
# o ''')    # Multi line
# print("""H
# e
# l
# l
# o """)    # Multi line

# name = "Tanya Jain"
# print(name[4]) # Using indexing
# print(name[4::2]) # slicing
# print(name[-1])
# print(name[-1:-5:-1])
# start = 0
# end = last
# step = +1
# print(name + " God")
# print((name + " ") * 4)
# print(2**2)
# print("n" not in name)

# dynamic string
# f-string
# user = input("Enter: ")
# input(f"What is your age {user}: ")
# input("What is your age %s %i: " %(user, 12)) 
# print(f"Hello {user}", user)

# name = "tanya jain, akshay sharma, harshit thakur, mohit kumar, piyush"

# name = name.replace(", ", ",")
# name[0]
# "tanya jain"[0]
# for i in range(0, len(name)):
#     if name[i] == ", ":
#         print()
#     else:
#         print(name[i], end="")

# for i in name:
#     if i == ",":
#         print()
#     else:
#         print(i, end="")

# name = "this is a notbook. this is a notbook. this is a notbook. this is a notbook. this is a notbook. this is a notbook. this is a notbook. this is a notbook. "
# print(name[8].upper())
# name = "Akshay"
# print(dir(name))