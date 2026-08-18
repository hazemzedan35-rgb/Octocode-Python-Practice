def main():
    mean = average(get_numbers())
    print(f"Mean is = {mean}")

def get_numbers():
    numb = []
    while True:
        try:
            numb_list = int(input("enter your number: "))

        except ValueError:
            continue

        except KeyboardInterrupt:
            break

        else:
            numb.append(numb_list)

    return numb

def average(list_of_numbers):
    if len(list_of_numbers) == 0:
        raise ValueError("no values were added")
    
    return sum(list_of_numbers) / len(list_of_numbers)


if __name__=="__main__":
    main()