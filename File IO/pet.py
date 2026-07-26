import csv

with open("pets.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("fixed.pets.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["pet"])
        writer.writeheader()
        for row in reader:
            if "" in row["name"]:
                name = row["name"].strip('"')
            else:
                name = row["name"]

            writer.writerow({"pet": f"{row['species']} {name}"})
                



                