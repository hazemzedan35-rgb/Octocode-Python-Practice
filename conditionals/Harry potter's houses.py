#more efficient program for determining the name of house in Harry potter series
name = input("what is the character name?!!").strip()
match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("who?!1")
