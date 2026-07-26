import csv 

with open("gryffindors.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("students_with_points.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "house", "house_points"])
        writer.writeheader()

        for row in reader:
            points = int(input("how many point student will get? "))

            writer.writerow({"name": row["name"], "house": row["house"]
                             , "house_points": points})

         
with open("students_with_points.csv", "r") as file:
    reader = csv.DictReader(file)
    gryffindor_points = 0
    for row in reader:
        if row["house"].lower() == "gryffindor":
            gryffindor_points += int(row["house_points"])

    print(gryffindor_points)

    with open("total.txt", "w") as f:
        f.write(f"Gryffindor gets {gryffindor_points}")