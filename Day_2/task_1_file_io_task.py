import csv
import json

students = [
    {"name": "Arun", "marks": 55},
    {"name": "Priya", "marks": 60},
    {"name": "Rahul", "marks": 72},
    {"name": "Divya", "marks": 88},
    {"name": "Karthik", "marks": 48},
]

# 1. Write names to a text file and read them with line numbers.
with open("names.txt", "w", encoding="utf-8") as file:
    for student in students:
        file.write(student["name"] + "\n")

with open("names.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}. {line.strip()}")

# 2. Create a CSV file and print students with marks above 60.
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerows(students)

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    above_60 = [
        f"{row['name']} {row['marks']}"
        for row in reader
        if int(row["marks"]) > 60
    ]

print("Above 60: " + " | ".join(above_60))

# 3. Save the same students as JSON and read them back.
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)

with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

print("From JSON: " + " | ".join(
    f"{student['name']} {student['marks']}"
    for student in loaded_students
))

# 4. Handle a missing file.
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("missing.txt -> File not found")