class People:
    def __init__(self, name):
        self.name = name


class Customer(People):

    def __init__(self, name, address=None):
        super().__init__(name)
        if address is None:
            address = []
        self.address = address
        self.__payment_details = {}

    def add_payment_details(self, address, card_num):
        self.__payment_details['address'] = address
        self.__payment_details['card_num'] = card_num


    def send_payment_details(self):
        return self.__payment_details
