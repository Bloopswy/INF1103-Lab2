def get_valid_input():
    stock = input("Enter the stock quantity: ").lower()
    if stock == "quit":
        return "quit"
    elif stock.isdigit():
        return int(stock)
    else:
        return "Error"

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax_rate = 0.1
    tax_amount = amount * tax_rate
    return round(tax_amount, 2)

def generate_report(total_units, failed_attempts):
    print ("Total Units Processed: ", total_units, "\n Number of Failed/Rejected Entries:", failed_attempts)


inventory = 0
failed_entries = 0
delivery_tax = 0

while inventory <=500:
    stock_input = get_valid_input()
    if stock_input == "quit":
        print(generate_report(inventory, failed_entries))   #generates the report if the user input "quit"
        print("Delivery Tax: $", round(delivery_tax,2))
        break

    elif stock_input == "Error": 
        failed_entries += 1
        print("error")

    else:
        inventory = process_delivery(inventory, stock_input)
        delivery_tax += calculate_tax(stock_input) 
        if inventory > 500:
            print("Inventory limit reached. Cannot add more stock.")









