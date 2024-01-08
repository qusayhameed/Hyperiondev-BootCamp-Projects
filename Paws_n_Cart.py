# This is a pet shop products cart

new_item = ""
removed_item = ""
total_cart_cost = 0
cart = []
pet_food_prices = []
# Show the menu to the user
pet_food_choice =["Cat Food","Dog Food","Cat Bed","Dog Bed","Wiskers cat food", "Kong", "Lucerne Hay", "Fish food" ]
print(f"Our Pet Shopping Today is:")
for food in pet_food_choice:
 print(f"{food}")
# Create a while loop for continuous user shopping options selection    
while True:
    menu = input(" Please select one number of options bellow:\n\
                1. Add Item \n\
                2. Remove Item \n\
                3. Update Item \n\
                4. Exit Cart\n\
                :\t")
    if menu == "1":
        new_item = input("Enter an item to add to the cart:")
        # Add the item to the cart
        cart.append(new_item)
        # Request the price for the added item
        item_price = input("Enter new item price:£")
        if item_price.isnumeric():                    
        # Add the item price to the list
          pet_food_prices.append(item_price)
        else:
            print("Enter only numbers")
        
    elif menu == "2":
        if cart : # Check first if there is an item in the Cart
            product_remove = input("Enter an item to remove:")
            # Iterate in the cart to check for the item and remove it 
            for index,item in enumerate(cart):
                if product_remove == item :
                    # Display the removed item and its price
                    print(f"The removed item is: {item} and its price is:£ {pet_food_prices[index]}")
                    cart.remove(item)
                    del pet_food_prices[index]
                else:
                    continue
        else:
            print("Your cart is empty")    

    elif menu == "3":
        print("Item updated")
        item_update = input("Which item you would like to update:")
        for index,item_change in enumerate(cart):
            if item_change == item_update:
                item_price = int(input("Enter new item price:£"))
                pet_food_prices[index] = item_price
                print(f"The updated item is {item_update} and the new price is {item_price}")

    elif menu == "4":
        # Iterate in all items added prices to calculate the total cart cost
        for i in pet_food_prices:
            total_cart_cost += int(i)
        print("My card contain : ", cart)
        print (f"Total cart cost is:£ {total_cart_cost}" )
        print("Today shopping is done!")
        break
    else:
        print("Invalid option")


