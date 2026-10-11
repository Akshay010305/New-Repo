# containsUpper = False
# containsLower = False
# containsSymbols = False
# while True:
#     password = input("Enter your password: ")
#     symbols = "!@#$%&"
#     if len(password)>=8:
#         if " " not in password:
#             for i in password: # abCd
#                 if i == i.upper(): # C==C
#                     containsUpper = True
#                     break
#             for i in password: # abCd
#                 if i == i.lower():
#                     containsLower = True
#                     break
#             for i in password: # abCd
#                 if i in symbols:
#                     containsSymbols = True
#                     break
#             if not(containsUpper): # C==C
#                 print("Your password is missing uppercase letters.")
#             if not(containsLower):
#                 print("Your password is missing lowercase letters.")
#             if not(containsSymbols):
#                 print("Your password is missing symbols.")

#             if containsUpper and containsLower and containsSymbols:
#                 print("Your password is absolute masterpiece")

#         else:
#             print("Your password contains spaces")
#     else:
#         print("Your password must be longer or equal to 8")

names = ["Akshay", "Aksha", "Bharti", "Kashish", "Harshit", "Tanya"]
# print(names[2])
# for i in range(len(names)): # len()
#     print(f"Their name is {names[i]}")

# for i in names:
#     if "ya" in i:
#         print(i)

# print(min(names))
# print(max(names))

names.append("Mohit")
names.extend(["Aryan", "Meher", "Khushboo"])
names.pop(1)
print(names)
# user = input("Enter your value: ")
# idx = names.index(user)
# print(idx)
# names.pop(idx)
# print(dir(names))
for i in dir(names):
    if "_" not in i:
        print(i)

# names.clear()
# print(names.count("Akshay"))
# user = input("Enter: ")
# idx = names.index(user)
# addValue = input("Enter adding: ")
# names.insert(idx+1, addValue)
# print(names)
# newName = names.copy()
# print(names)
# newName.clear()
# print(newName)
# print(names)
# names.sort()
# print(names)

# print("""
#       1. Create
#       2. Read
#       3. Update
#       4. Delete
#       5. Insert

#       """)
# li = []
# choice = int(input("Enter: "))

# values = []
# # print(values)
# sum = 0

# size = int(input("Enter the grid size: "))
# for i in range(size):
#     values.append([])
    
# print(values)

# for row in range(size):
#     for col in range(size):
#         values[row].append(int(input(f"Enter row: {row} col: {col} :")))


# for row in range(len(values)):
#     print("|", end=" ")
#     for col in range(len(values[row])):
#         print(values[row][col], end=" ")
#     print("|")

# while True:
#     print("""
#       1. Create
#       2. Read
#       3. Update
#       4. Delete
#       5. Insert
#       0. Exit
#       """)
#     choice = int(input("Enter: "))
#     if choice==0:
#         print("Bye")
#         break

tup = (12,34,45,56,76)
print(tup)
tup
print(tup)