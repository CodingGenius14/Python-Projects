# Check Out Register Program
import os
print("Welcome to Save-A-Lot")
date = input("Enter Date: ")
register_number = input("Enter Register Number: ")
sales_associate_id = input('Enter Sales Associate ID: ')
more_items = "Y"
another_customer = "1"
items = []
items_price = []
customer_total_price = 0
register_total_price = 0
customer = 1


def clear():
    os.system('cls')


while another_customer == "1":
    while more_items == "Y":
        print(f"Customer #{customer}\nScan Item:")
        item = input("\tItem Name: ")
        item_price = float(input("\tPrice: "))
        num_of_items = int(input("\tHow Many: "))
        items.append(item)
        items_price.append(item_price * num_of_items)
        more_items = input("More Items? Enter (y) for Yes or (n) for No: ").upper()
        clear()

    print("\tWelcome to Save-A-Lot")
    print(f"Date: {date}\tRegister:{register_number}")
    print(f"Sales Associate: {sales_associate_id}\n")

    for i in range(len(items)):
        print(f"{items[i]}\t${items_price[i]}")
        customer_total_price += items_price[i]

    register_total_price += customer_total_price

    print(f"Total Items: {len(items)}")
    print(f"Your total is ${customer_total_price}")
    print("Thank you, Come Again Soon")

    print("=" * 50)

    another_customer = input("Enter 1 - For another customer | Enter 2 - Close Register: ")
    clear()
    if another_customer == '1':
        print("Next Customer")
        customer += 1
        items_price.clear()
        items.clear()
        customer_total_price = 0
        more_items = "Y"

clear()
print(f"Sales Report for: {sales_associate_id}\n")
print(f"Number of customers served: {customer}")
print(f"Total sales for register {register_number}: ${register_total_price}")
