class Coffee:
    # Class variable to keep track of all coffees
    all_coffees = []

    def __init__(self, name):
        # Use the property setter for validation
        self._name = None  # Internal storage for name
        self.name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Only allow setting name once (immutable after creation)
        if self._name is not None:
            raise AttributeError("Coffee name cannot be changed after creation.")
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    def orders(self):
        # Import here to avoid circular imports
        from order import Order
        # Return all orders for this coffee
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        # Return unique list of customers who ordered this coffee
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        # Return the number of orders for this coffee
        return len(self.orders())

    def average_price(self):
        # Return the average price of this coffee across all orders
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)