import os

inventory = ["Sword", "Armor", "Shield"]

print("Hero's Inventory:\n\nWhere you can exchange and add your tools and weapons to get the items you want to use to fight the enemy\n")
print("Current Hero's Inventory:\n")
for i in range(len(inventory)):
    print(f"{i + 1}: {inventory[i]}\n\n")

trade = input("Would you like to trade your item for anything else?\nType (y) for yes or (n) for no: ").upper()
print()

if trade == "Y":
    item_number_index = int(input(
        "What item do you want to remove from your current inventory?\nPlease enter the number of the item see above: ")) - 1
    print()
    print(f"What item would you like to replace your {inventory[item_number_index]}")
    new_item = int(
        input("Choose the number from the options below:\n1-Magic Potion\t2-Battle Axe\t3-Liquid Metal Shield: "))
    print()
    if new_item == 1:
        print("Item to add Magic Potion\n")
        inventory[item_number_index] = "Magic Potion"
    elif new_item == 2:
        print("Item to add Battle Axe\n")
        inventory[item_number_index] = "Battle Axe"
    else:
        print("Item to add Liquid Metal Shield\n")
        inventory[item_number_index] = "Liquid Metal Shield"

    os.system('clear')

    print("The items in your current inventory are:\n")
    for i in range(len(inventory)):
        print(f"{i + 1}: {inventory[i]}")

    print()

    add_items = input("Would you like to to add items to your inventory? (y) Yes or (n) No: ").lower()
    os.system('clear')

    if add_items == "y":
        while len(inventory) < 5:
            print(f"There is room to add {5 - len(inventory)} items to your inventory\n")
            item_to_add = input("What item would you like to add? ")
            print()
            inventory.append(item_to_add)

        os.system('clear')

        print("Your inventory is now currently filled!\nYour current inventory is:")
        for i in range(len(inventory)):
            print(f"{i + 1}: {inventory[i]}\n\n")

        final_swap = input("Would you like to make a final swap in your inventory? (y) for Yes (n) for No: ").lower()
        print()

        if final_swap == "y":
            final_swap_item = input(
                "What item do you want to swap out? (Type the item the way it is seen in the inventory) ")
            item_to_place = input("What item do you want to replace it with? ")
            inventory[inventory.index(final_swap_item)] = item_to_place
            os.system('clear')

            print("Here is your final inventory:")
            for i in range(len(inventory)):
                print(f"{i + 1}: {inventory[i]}")

print("Thank you for visiting the Hero's Inventory")


