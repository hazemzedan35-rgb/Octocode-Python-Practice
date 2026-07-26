import csv

students = []

with open("students..csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

for student in students:
    student["house_points"] = int(student["house_points"] )

def get_points(student):
    return student["house_points"]

sorted_students = sorted(students, key=get_points, reverse=True)

with open("sorted.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "house", "house_points"])
    writer.writeheader()

    for list in sorted_students:
        writer.writerow(list)