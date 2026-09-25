def load_inventory():
    with open("orders.txt", "r") as file:
        orders = file.readlines()
    return orders

def save_inventory(orders):
    with open("orders.txt", "w") as file:
        file.writelines(orders)









