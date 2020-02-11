#as a restaurant owner i can create new orders with food item for a customer

class Order():
    def __init__(self, customer):
        self.items = []
        self.customer = customer
        self.status = 'Open'

    def add_item_order(self, item):
        self.items.append(item)

    #have a method to calculate total

    #Have a method to pay, and change status.