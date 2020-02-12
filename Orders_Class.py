# as a restaurant owner i can create new orders with food item for a customer
from Food_item_class import *


class Order():
    def __init__(self, customer):
        self.items = []
        self.customer = customer
        self.status = 'Open'

    def add_item_order(self, item):
        self.items.append(item)

    # have a method to calculate total
    def total_price(self, food_list={}):
        #TODO Ask about how to implement the method in run.py
        self.food_list = {'Pizza': 10, 'Pasta': 25, 'Spaghetti': 20}
        total = 0
        for item in self.food_list:
            total = total + food_list[item]
        print(f'The price total is ${total}')

    # Have a method to pay, and change status.


# item1 = FoodItem('Pizza', 10, ['pizza'])
# item2 = FoodItem('Pasta', 10, ['pasta'])
# my_list = Order('Hamza')
# my_list.add_item_order(item1)
# my_list.add_item_order(item1
item1 = Order('hamza')
item1.total_price(food_list={'Pasta': 10, 'Pizza': 25, 'Spaghetti': 25})
