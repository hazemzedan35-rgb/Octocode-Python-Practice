# 1- perform a task 
def great(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome aboard")
great("mosh", "hamedani")

# 2- return a value 
def get_greating(name):
    return f"hi {name}"

message = get_greating("mosh")
print(message)

def square(x):
    result = x * x
    return result

print(square(int(input("what number do you have"))))