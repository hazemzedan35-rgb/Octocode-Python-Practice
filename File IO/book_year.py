import csv 

books = []

with open("books..csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        books.append(row)


def get_books(book):
    return book["author"]

sorted_books = sorted(books, key=get_books, reverse= False)

with open("sorted_books.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames= ["title", "author", "year"])
    writer.writeheader()

    for list in sorted_books:
        writer.writerow(list)