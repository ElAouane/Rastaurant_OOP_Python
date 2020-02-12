
class FoodItem():


    def __init__(self, item, price, ingredients=None):
        self.item = item
        self.price = price
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients


    @classmethod
    def get_inputs(cls):
        #TODO list Check if you can update the list
        food_inputs = {}
        food_inputs['food_item'] = input('Insert the dish name: ')
        food_inputs['food_price'] = float(input('Insert the price'))
        food_inputs['ingredients'] = input('Insert the ingrediends').split("-")
        FoodItem.ingredients = [food_inputs['ingredients']]
        return food_inputs

        # as for user inputs
        # build a dictionary
        # return dictionary

        # optional route that is bit more integrate
        # after getting inputs
        # create a instance
        # return the intance


# class Side(Food_item):
#     pass
#
#
# class Main(Food_item):
#     pass


class Combos(FoodItem):
    def __init__(self, item, price, list_individual_items=None, ingredients=None):
        super().__init__(item, price, ingredients)
        if list_individual_items is None:
            list_individual_items = []
        self.list_individual_items = list_individual_items


#FoodItem.get_inputs();
