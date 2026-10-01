def load_inventory():
    file = open("inventory.txt", "a")
    file.close()

    with open("inventory.txt", "r") as file:
        inventory = file.readlines()

    return inventory


def save_inventory(inventory):
    with open("inventory.txt", "w") as file:
        file.writelines(inventory)


def get_valid_input():
    quantity = input("Enter Quantity: ")

    if quantity.isdigit():
        return int(quantity)
    else:
        return "Error"



inventory = load_inventory() #list


print("Current Inventory: \n")

if len(inventory) == 0:
    print("No items in inventory.")
else:
    for item in inventory:
        print(item.strip())

current_id = 1001 #set first id number as 1001



while True:
    product_input = input("Enter Product Name: ")

    if product_input.lower() == "quit":
        break

    quantity = get_valid_input() #if no "quit" continue asking for quantity

    if quantity == "Error":
        print("Invalid quantity")
        continue

    new_id = current_id + len(inventory) #id number starts from 1001 + [0, 1, 2, 3...]

    new_item = str(new_id) + "," + product_input + "," + str(quantity) + "\n"

    inventory.append(new_item)

    print("New Item Added:")
    print(new_item.strip())
    save_inventory(inventory) #save inventory to file after each new item is added
    print("Inventory successfully saved to inventory.txt")


save_inventory(inventory)

