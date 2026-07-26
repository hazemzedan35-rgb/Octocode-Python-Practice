import csv 

with open("_students.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("gryffindors.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "house"])
        writer.writeheader()
        for row in reader:
            if row["house"].lower() == "gryffindor":
                writer.writerow({"name": row["name"], "house": row["house"]})
