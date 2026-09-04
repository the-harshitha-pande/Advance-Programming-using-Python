"""
#student file marks record
marks = [25,35,90,"ab",45,"pranav"]
updated_marks = [25,35,90,45]
handle this exception and give this updated marks
"""
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

#
marks = [25,35,90,"ab",45,"pranav"]
updated_marks = []
for i in marks:
    try:
        updated_marks.append(int(i))
    except ValueError as error:
        print("Error to update marks. Enter numbers only:", error)
        continue
print("Updated marks:", updated_marks)

#user input marks and handle exception
marks = input("Enter marks separated by commas: ").split(",")
updated_marks = []
for i in marks:
    try:
        updated_marks.append(int(i))
    except ValueError as error:
        print("Error to update marks. Enter numbers only:", error)
        continue
print("Updated marks:", updated_marks)
