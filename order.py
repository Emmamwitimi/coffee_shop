# order.py

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        # Append to the class-level _orders list in both Customer and Coffee classes
        Customer._orders.append(self)
        Coffee._orders.append(self)

    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
