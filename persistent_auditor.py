def load_inventory():
    file = open("orders.txt", "a")
    file.close()

    with open("orders.txt", "r") as file:
        orders = file.readlines()

    return orders


def save_inventory(orders):
    with open("orders.txt", "w") as file:
        file.writelines(orders)


def get_valid_input():
    quantity = input("Enter Quantity: ")

    if quantity.isdigit():
        return int(quantity)
    else:
        return "Error"


orders = load_inventory() #list

print("Current Orders: \n")

current_id = 1001 #set first id number as 1001

for order in orders:
    order = order.strip()
    print(order)


while True:
    product_input = input("Enter Product Name: ")

    if product_input.lower() == "quit":
        break

    quantity = get_valid_input() #if no "quit" continue asking for quantity

    if quantity == "Error":
        print("Invalid quantity")
        continue

    new_id = current_id + len(orders) #id number starts from 1001 + [0, 1, 2, 3...]

    new_order = str(new_id) + "," + product_input + "," + str(quantity) + "\n"

    orders.append(new_order)

    print("New Order Added:")
    print(new_order.strip())
    print("Orders successfully saved to orders.txt")


save_inventory(orders)

