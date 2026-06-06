# ==  equality
# !=  not equal
x = int(input("what's the n.x "))
y = int(input('whats the n.y ')) 
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
# or statement
if x > y or x < y:
    print("x is not equal to y")
# simpiler form of code
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
# the word and 
score = int(input("score: "))
if score >= 90 and score <=100:
    print("you got A ")
elif score >= 80 and score <=89:
    print("you got B ")
elif score <= 70 and score >= 79:
    print ("you got C")
elif score <= 60 and score >= 69:
    print("you got D ")
else:
    print("you got F")
# more simpler code 
score = int(input("score: "))
if 90 <= score <=100:
    print("you got A ")
elif 80 <= score <=89:
    print("you got B ")
elif 70 <= score <= 79:
    print ("you got C")
elif 60 <=  score <= 69:
    print("you got D ")
else:
    print("you got F")
# % operator 
# determine if the number is even or not 
x = int(input("what is the value of x? "))
if x % 2 == 0:
    print("x is even ")
else:
    print("x is odd")

# determining the name of house in Harry potter series
name = input("what is the character name ?\n")
if name == "Harry" or name == "Hermoine" or name =="Ron":
    print("Gryffindor")
elif name == "draco":
    print("slytherin")
else:
    print("who?!!")
# more efficient program for determining the name of house in Harry potter series
name = input("what is the character name?!!")
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who?!!!")
