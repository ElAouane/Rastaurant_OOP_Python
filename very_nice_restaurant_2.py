from People_class import People, Customer
from Food_item_class import FoodItem, Combos
from Orders_Class import Order

# We want a game to keep running
#   Create a simple switch board

# We need the following options:
#   as a user i can create customers
#   as a user i can create food items
#   as a user i can create orders (depends on selecting a user)
#   as a user i can add items to order (requests a specific order and selecting of food items)
#   as a use i can see the total of an order (requires a calculating the total of all the food)


customer_list = []
food_list = []
while True:
    pass

    # Print options
    print("Where would you like to go? \n "
          "1 - Create a Customer \n "
          "2 - Create Food \n "
          "3 - Go to the check out")
    user_input = input('>>>>')
    # Get user input
    if user_input == '1' or 'create customer' in user_input.lower():
        #Get user input for x or y
        #use it to create a customer
        print('Please input Name and Address')
        customer_name = input("Please, input customer name: ")
        customer_address = input("Please, input customer address")
        customer = Customer(f'{customer_name}', f'{customer_address}' )
        customer_list.append(customer)
        for item in customer_list:
            print(item.name + ' ' + item.address)
    elif user_input == '2' or 'create food' in user_input.lower():
        #TODO Check if after every input the dict is updated and the total price is collable later
        FoodItem.get_inputs()
        # print("What dish would you like to create?Input Item- Price- Ingredient")
        # food_item = input('Insert the dish name: ')
        # food_price = int(input('Insert the price'))
        # food_ingredients = input('Insert the ingrediends').split("-")
        # FoodItem.ingredients = [food_ingredients]
        # food = FoodItem(f'{food_item}', f'{food_price}', f'{food_ingredients}')
        # food_list.append(food)
        # for food in food_list:
        #     print(food.item + ',' + food.price + ',' + food.ingredients)
    elif user_input == '3' or 'check out' in user_input.lower():
        Order.total_price(food_list= FoodItem.get_inputs())

#   Evaluate and go to each option
#       Inside each option, do logic and create what ever you need to create


