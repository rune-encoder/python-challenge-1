# This function just styles the terminal when running the code. 
def print_custom(text, color='35', border=False):
    border_line = "\n" + ('=' * 42) if border else ""
    return print(f"\033[{color}m{text:^{42}}" + f"{border_line}\033[0m")

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
orders_list = []

# Launch the store and present a greeting to the customer
print_custom("Welcome to the variety food truck!", border=True)

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print_custom("From which menu would you like to order?", color="36")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print_custom(f"What {menu_category_name} item would you like to order?", color="36")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            menu_selection = input(f"Type the order number from our list of {menu_category_name.lower()}: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items:
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]
                    item_price = menu_items[menu_selection]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name.lower()}(s) would you like to order?\nNote: Pressing enter will default to 1:")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        # Add the item name, price, and quantity to the order list
                        quantity = int(quantity)
                        orders_list.append({
                            "Item name": item_name,
                            "Price": item_price,
                            "Quantity": quantity
                        })
                    else:
                        quantity = 1

                    # Tell the customer that their input isn't valid
                else:
                    print_custom(f"'{menu_selection}' is not an option in our {menu_category_name.lower()} menu.", color="31")

                # Tell the customer they didn't select a menu option
            else:
                print_custom("You didn't select a number.", color="31")

        else:
            # Tell the customer they didn't select a menu option
            print_custom(f"'{menu_category}' was not a menu option.", color="31")
    else:
        # Tell the customer they didn't select a number
        print_custom("You didn't select a number.", color="31")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input(
            "Would you like to keep ordering? (Y)es or (N)o ").lower().strip()

        # 5. Check the customer's input
        match keep_ordering:
            case "y":
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break
            case "n":
                # Complete the order
                place_order = False
                # Since the customer decided to stop ordering, thank them for
                # their order
                print_custom("Thank you for your order!", border=True)
                # Exit the keep ordering question loop
                break
            case _:
                # Tell the customer to try again
                print_custom(f"'{keep_ordering}' is not a valid input. Please try again!", color="31")

# Print out the customer's order
print_custom("This is what we are preparing for you...\n", color="36")

# Uncomment the following line to check the structure of the order
# print(orders_list)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for order in orders_list:

    # 7. Store the dictionary items as variables
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(item_name)

    # 9. Create space strings
    item_spaces = " " * num_item_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}|{'$' + str(price):^8}|{' ' + str(quantity):<10}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum([order["Price"] * order["Quantity"] for order in orders_list])
print_custom(f"\nTotal Cost: {total_cost:.2f}", color="33", border=True)
