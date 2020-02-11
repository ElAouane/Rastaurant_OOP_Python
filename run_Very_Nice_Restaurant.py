from People_class import People, Customer
from Food_item_class import *

# As a restaurant owner i can create new customers
customer1 = Customer('John', '21 down town Abi, London')
customer2 = Customer('Anabela', 'Hackney, London')

# as a restaurant owner i can create new orders with food item for a customer
# 3 Mains
main1 = FoodItem('Sea Bass', 17.5, ['Sea bass fish'])
main2 = FoodItem('Omlette du Fromage Avec Champignon', 9, ['Eggs', 'Cheese', 'Mushroom'])
main3 = FoodItem('Fiorentina', 5.5, ['Tomato Sauce', 'Mozzarell', 'Parmisan', 'Fresh Spinach'])
# 3 Sides
side1 = FoodItem('Garlic Bread', 4, ['Bread', 'Garlic', 'Oregano'])
side2 = FoodItem('Garlic Cheese Bread', 4, ['Bread', 'Garlic', 'Oregano', 'Cheese'])

# 3 drinks
drink1 = FoodItem('Water', 2, ['Water'])
drink2 = FoodItem('Cocacola', 3, ['Others'])
drink3 = FoodItem('Smoothies', 4, ['Orange', 'Carrots', 'Kiwi'])

# 3 Combos

