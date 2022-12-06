import csv
from datetime import datetime

def read_dict(filename, index_val):
    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:

                key = row_list[index_val]

                dictionary[key] = row_list

    return dictionary
def calculate_total_items(numbers_list):
    total =0
    for number in numbers_list:
        total = int(number) + total
    return total

def calc_total(amounts, prices):
    counter = 0
    total_p = 0
    for i in amounts:
        num1 = float(i)
        num2 = float(prices[counter])
        total_p = (num1 * num2) + total_p 
        counter = counter +1
    return round(total_p,2)

def main(store_items,cart_items):
    store = read_dict(store_items,0)
    items = []
    quantities =[]
    with open(cart_items, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)
        for row_list in reader:
            items.append(row_list[0])
            quantities.append(row_list[1])
    total_items = calculate_total_items(quantities)
    
    final_items = []
    final_price = []
    for products in items:
        if products in store:
            line =store[products]
            final_items.append(line[1])
            final_price.append(line[2])
        else:
            raise KeyError 
    total_price = (calc_total(quantities,final_price))
    sales_tax = round((total_price * .06),2)
    final_total = total_price + sales_tax
    current_date_and_time = datetime.now()

    print("Inkom Emporium ")
    print()
    counter = 0
    for i in items:
        print(str(final_items[counter]) + ": " + quantities[counter] + " @ $" + str(final_price[counter]) + " each")
        counter = counter+1

    print()
    print("Number of items: "+ str(total_items))
    print("Subtotal: $" + str(total_price))
    print("Sales tax: $" + str(sales_tax))
    print("Total: $" + str(final_total))
    print()
    print("Thank you for shopping at Inkom Emporium.")
    print(f"{current_date_and_time:%A %b %d %I:%M %p %Y}")

try:
    store = input("What is the name of the CSV file with the stores goods? ")
    want = input("What is the name of the CSV file with the items you want? ")
    main(store,want)
except FileNotFoundError:
    print()
    print(f"The {store}  or {want} files doesn't exist.")
    print("Run the program again and enter the" \
        " name of an existing file.")
except PermissionError:
    print()
    print(f"You don't have permission to read either the {store} or {want}.")
    print("Run the program again and enter the name" \
        " of a file that you are allowed to read.")
except KeyError:
    print()
    print("Unknown product ID in the request.csv file")
