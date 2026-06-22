while True:
    try:
        x = int(input("what is x?\n"))

    except ValueError:
        pass

    else:
        try:
            result = 100 / x
            print(f"result is {result}")
            break
        
        except ZeroDivisionError:
            pass
            