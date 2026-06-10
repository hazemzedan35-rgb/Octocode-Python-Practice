def convert(time):
   Hours, minutes = time.split(":")
   return float(Hours) + float(minutes) / 60
def main():
    amount_time = convert(input("how many time did you spent\n")) 
    if amount_time > 3:
        return (amount_time *20) - 10
    elif amount_time < 3:
        return f"total spent is: {amount_time * 20}"
print(main())

    
