# Assignment:
# You got a job at Python Pizza, your first job is to build an automated pizza order program.
# Based on a customer's order, work out their final bill.

# Menu Prices:
# - Small pizza: $15
# - Medium pizza: $20
# - Large pizza: $25

# Additional Charges:
# - Pepperoni for small pizza: +$1
# - Pepperoni for medium or large pizza: +$2
# - Extra cheese for any pizza: +$1

# Example Input:
# - Size:
#   - Small pizza: "S"
#   - Medium pizza: "M"
#   - Large pizza: "L"
# - Add Pepperoni: "Yes", "No"
# - Add Extra Cheese: "Y", "N"

# Example Output:
# Your final bill is: $50

# Welcome message
print("Hi, Welcome to Python Pizza\n")

# Initialize price and receipt dictionary
price_total = 0
receipt = {
    'Pizza': {'Small': 0, 'Medium': 0, 'Large': 0},
    'Topping': {'Pepperoni': 0, 'Extra Cheese': 0},
    'Total': 0
}

while True:
    # Main menu options
    print("Options:\n")
    print("1. Order Pizza")
    print("2. Cancel\n")
    
    try:
        menu_option = int(input("Choose from the options above: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        continue
    
    if menu_option not in [1, 2]:
        print("Please choos from the valid options")
    elif menu_option == 1:
        
        while True:
            # Pizza size selection
            print("\nChoose Pizza Size:")
            print("1. Small ($15)")
            print("2. Medium ($20)")
            print("3. Large ($25)")
            print("4. Checkout")
            print("5. Cancel order\n")
            
            try:
                order_pizza_options = int(input("Select an option: "))
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                continue
            
            if order_pizza_options not in [1, 2, 3, 4, 5]:
                print("\nPlease choose from the valid options ")
            
            elif order_pizza_options in [1, 2, 3]:
                # Add pizza to order
                size = ""
                if order_pizza_options == 1:
                    size = 'Small'
                    receipt['Pizza']['Small'] += 1
                    price_total += 15
                elif order_pizza_options == 2:
                    size = 'Medium'
                    receipt['Pizza']['Medium'] += 1
                    price_total += 20
                elif order_pizza_options == 3:
                    size = 'Large'
                    receipt['Pizza']['Large'] += 1
                    price_total += 25
                
                print(f"\n{size} size Pizza added to order.")
                
                while True:
                    # Topping selection
                    print("\nChoose Toppings:")
                    print("1. Pepperoni ($1 for Small, $2 for Medium/Large)")
                    print("2. Extra Cheese ($1)")
                    print("3. No Toppings")
                    print("4. Previous Menu\n")
                    
                    try:
                        topping = int(input("Select an option: "))
                    except ValueError:
                        print("\nInvalid input. Please enter a number.")
                        continue
                    
                    if topping == 4:
                        break
                    elif topping == 3:
                        print("\nReturning to previous menu.")
                        break
                    elif topping == 1:
                        # Add pepperoni
                        if order_pizza_options == 1:
                            receipt['Topping']['Pepperoni'] += 1
                            price_total += 1
                        else:
                            receipt['Topping']['Pepperoni'] += 1
                            price_total += 2
                        print("\nPepperoni added.")
                    elif topping == 2:
                        # Add extra cheese
                        receipt['Topping']['Extra Cheese'] += 1
                        price_total += 1
                        print("\nExtra cheese added.")
                    
                    more_toppings = input("\nDo you want more toppings? Yes(1), No(2): ")
                    if more_toppings == '1':
                        continue
                    else:
                        break

            elif order_pizza_options == 4:
                # Check if user ordered 
                if price_total == 0:
                    print("\nYou have not ordered anything yet.")
                    continue
                else:
                    # Print receipt
                    print("\nReceipt:\n")
                    for key, value in receipt['Pizza'].items():
                        if value > 0:
                            print(f"{value} x {key} Pizza")
                    for key, value in receipt['Topping'].items():
                        if value > 0:
                            print(f"{value} x {key}")
                    print(f"\n\tTotal: ${price_total}\n")
                break

            elif order_pizza_options == 5:
                print("\nOrder cancelled. Have a nice day!")
                break
        break
    elif menu_option == 2:
        print("\nHave a nice day!")
        break
    






 



    




