class FoodItem():
    def __init__(self, item, price, ingredients=None):
        self.item = item
        self.price = price
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients


# class Side(Food_item):
#     pass
#
#
# class Main(Food_item):
#     pass


class Combos(FoodItem):
    def __init__(self, item, price, list_individual_items = None, ingredients=None):
        super().__init__(item, price, ingredients)
        if list_individual_items is None:
            list_individual_items = []
        self.list_individual_items = list_individual_items
