import random
import datetime
from collections import Counter
from functools import reduce

students = {
    "Tarun": [82, 91, 78],
    "Karthik": [65, 72, 68],
    "Chadrika": [91, 95, 89],
    "Trisha": [76, 81, 79],
    "Atul": [88, 84, 92]
}

averages = {}

for name, marks in students.items():
    total = reduce(lambda x, y: x + y, marks)
    average = total / len(marks)
    averages[name] = average

highest_student = max(averages, key=averages.get)
highest_average = averages[highest_student]

selected_student = random.choice(list(students.keys()))

current_date = datetime.date.today()

grades = []

for average in averages.values():
    if average >= 90:
        grades.append("A")
    elif average >= 80:
        grades.append("B")
    elif average >= 70:
        grades.append("C")
    elif average >= 60:
        grades.append("D")
    else:
        grades.append("F")

grade_count = Counter(grades)

print("===== STUDENT PERFORMANCE ANALYZER =====")

for name, average in averages.items():
    print(name, "Average:", round(average, 2))

print("\nHighest Average:")
print(highest_student, "-", round(highest_average, 2))

print("\nRandomly Selected Student:")
print(selected_student)

print("\nCurrent Date:")
print(current_date)

print("\nGrade Classification:")
print(grade_count)

import sys
import random
import datetime
from collections import defaultdict
from itertools import combinations
from functools import reduce

students = [
    ("Anita", "CSE", 85),
    ("Rahul", "CSE", 78),
    ("Priya", "CSE", 92),
    ("Kiran", "CSE", 88),
    ("Arjun", "AI", 81),
    ("Meena", "AI", 90),
    ("Ravi", "AI", 76),
    ("Sneha", "Data Science", 87),
    ("Vijay", "Data Science", 79),
    ("Neha", "Data Science", 94),
    ("Asha", "Cyber Security", 83),
    ("Rohan", "Cyber Security", 89)
]

if len(sys.argv) < 2:
    print("Usage: python allocation.py <team_size>")
    sys.exit()

team_size = int(sys.argv[1])

departments = defaultdict(list)

for student in students:
    name, department, marks = student
    departments[department].append((name, marks))

print("===== PROJECT TEAM ALLOCATION =====")
print("Team Size:", team_size)

for department, student_list in departments.items():

    if len(student_list) < team_size:
        print("\nDepartment:", department)
        print("Not enough students to form a team.")
        continue

    possible_teams = list(combinations(student_list, team_size))

    selected_team = random.sample(possible_teams, 1)[0]

    marks = [student[1] for student in selected_team]

    total_marks = reduce(lambda x, y: x + y, marks)

    average_marks = total_marks / len(selected_team)

    allocation_date = datetime.date.today()

    print("\nDepartment:", department)
    print("Selected Team:")

    for i, student in enumerate(selected_team, start=1):
        print(i, ".", student[0], "-", student[1])

    print("Total Marks:", total_marks)
    print("Average Marks:", format(average_marks, ".2f"))
    print("Allocation Date:", allocation_date)