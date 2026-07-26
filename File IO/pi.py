import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)


    with open("cleaned.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house"])
        writer.writeheader()

        for row in reader:
            if "," in row["name"]:
                last, first = row["name"].split(", ")
                name = f'{first} {last}'
    
            else:
                name = row["name"]

            writer.writerow({"name": name,
                             "house": row["house"]
                             })