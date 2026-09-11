inventory = 0
failed_entries = 0

while inventory <=  500:
    stock = input("Enter the stock quantity: ").lower()
    if stock == "quit":
        print("Total Units Processed: ", inventory, "\n Number of Failed/Rejected Entries:", failed_entries)
        break

    elif stock.isdigit():
        inventory = inventory + int(stock)
        if inventory > 500:
            print("Inventory limit reached. Cannot add more stock.")
    else:
        failed_entries = failed_entries + 1
        print("error") 









