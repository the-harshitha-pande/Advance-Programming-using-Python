##EXCEPTION HANDLING
"""
#student file marks record
marks = [25,35,90,"ab",45,"pranav"]
updated_marks = [25,35,90,45]
handle this exception and give this updated marks
"""

#this method dosnt work as it will break the loop when exception occurs
# try:
#     marks = [25,35,90,"ab",45,"pranav"]
#     updated_marks = []
#     for i in marks:
#             updated_marks.append(int(i))
#     print("Updated marks:", updated_marks)
# except ValueError as error:
#     print("Error to update marks. Enter numbers only:", error)
#     print("Updated marks:", updated_marks)

#     try:
#         original_marks=[int, updated_marks]
#         for i in marks:
#             original_marks.append(int(i))
#     except ValueError as error:
#         print("Error to update marks. Enter numbers only:", error)

#     print("Original marks:", original_marks)

#do this to file also
# marks = [25,35,90,"ab",45,"pranav"]
# updated_marks = []
# for i in marks:
#     try:
#         updated_marks.append(int(i))
#     except ValueError as error:
#         print("Error to update marks. Enter numbers only:", error)
#         continue
# print("Updated marks:", updated_marks)

# #file:
# valid_marks=[]
# with open("marks.txt", "r") as file:
#     for line in file:
#         try:
#             if marks>0 
#             valid_marks.append(int(line.strip()))
#         except ValueError as error:
#             print("Error to update marks. Enter numbers only:", error)
#             continue

# #user input marks and handle exception
# marks = input("Enter marks separated by commas: ").split(",")
# updated_marks = []
# for i in marks:
#     try:
#         updated_marks.append(int(i))
#     except ValueError as error:
#         print("Error to update marks. Enter numbers only:", error)
#         continue
# print("Updated marks:", updated_marks)

#trying to withddraw money when balance is 0 . suppose balance was 5000 and u withdrawed 5000 and now balance is 0 and u try to withdraw 1000 then it should give error and negative value should not be allowed error should be handled
balance=int(input("Enter your balance: "))
deposit = int(input("Enter the amount to deposit: "))
try:
    if deposit <= 0:
        raise ValueError("Deposit amount cannot be negative or zero")
    else:
        balance += deposit
        print("Deposit successful:", balance)
except ValueError as error:
    print("Error:", error)
withdrawal=int(input("Enter the amount to withdraw: "))
try:
    if withdrawal>balance:
        raise ValueError("withdrawal amount exceeding the existing balance")
    elif withdrawal <= 0:
        raise ValueError("withdrawal amount cannot be negative or zero")
    else:
        balance-=withdrawal
        print("Withdrawal successful:", balance)
except ValueError as error:
    print("Error:", error)