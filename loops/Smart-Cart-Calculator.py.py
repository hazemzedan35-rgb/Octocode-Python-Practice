print("***welcome to Ishop calculator***")
number_items = int(input("How many items are there in your basket today?\n"))
items_names_list = []
items_price_list = []
print("lets get to counting them")


for item in range(1,number_items + 1):
    name_of_items = input(f"please tell me the name of the item number {item}\n").strip()
    price_items = int(input(f"what is the price of {name_of_items}\n$").strip())
    items_price_list.append(price_items)
    items_names_list.append(name_of_items)


seeing_items = input("would you like see your basket's items? (yes, no)\n").strip().lower()
if seeing_items == "yes":
    print(items_names_list)
else:
    print("ok!")
seeing_total_price = input("would you like see their total price? (yes, no)\n").strip().lower()
if seeing_total_price == "yes":
    print(f"buying these items costs ${sum(items_price_list)}")
else:
    print("ok, have a nice day")
