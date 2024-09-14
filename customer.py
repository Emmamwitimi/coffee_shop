# customer.py

class Customer:
    _orders = []  # This will hold all order instances

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        # Return all orders for this customer
        return [order for order in Customer._orders if order.customer == self]

    def coffees(self):
        # Return a unique list of coffees this customer has ordered
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        # Create a new order and associate it with this customer and the coffee
        new_order = Order(self, coffee, price)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        # Dictionary to hold each customer's total spend on this coffee
        customer_spendings = {}

        # Iterate over all orders and sum the total price for each customer for the given coffee
        for order in cls._orders:
            if order.coffee == coffee:
                customer = order.customer
                if customer not in customer_spendings:
                    customer_spendings[customer] = 0
                customer_spendings[customer] += order.price

        # If no customers ordered this coffee, return None
        if not customer_spendings:
            return None

        # Find the customer who spent the most
        return max(customer_spendings, key=customer_spendings.get)
