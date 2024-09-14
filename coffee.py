# coffee.py

class Coffee:
    _orders = []  # This will hold all order instances (assumes central tracking of orders)

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = value

    def orders(self):
        # Return all orders for this coffee
        return [order for order in Coffee._orders if order.coffee == self]

    def customers(self):
        # Return a unique list of customers who ordered this coffee
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        # Return the total number of orders for this coffee
        return len(self.orders())

    def average_price(self):
        # Calculate and return the average price of this coffee's orders
        total_price = sum(order.price for order in self.orders())
        if self.num_orders() == 0:
            return 0
        return total_price / self.num_orders()
