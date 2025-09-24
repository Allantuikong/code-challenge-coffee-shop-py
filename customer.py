class Customer:
    # Class variable to keep track of all customers
    all_customers = []

    def __init__(self, name):
        # Use the property setter for validation
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Validate: must be a string, 1-15 chars
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1-15 characters long.")
        self._name = value

    def orders(self):
        # Import here to avoid circular imports
        from order import Order
        # Return all orders for this customer
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        # Return unique list of coffees this customer has ordered
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        # Create a new order for this customer
        from order import Order
        return Order(self, coffee, price)