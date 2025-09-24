class Order:
    # Class variable to keep track of all orders
    all_orders = []

    def __init__(self, customer, coffee, price):
        # Validate price: must be float, 1.0 <= price <= 10.0
        if not isinstance(price, (float, int)):
            raise ValueError("Price must be a number.")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = float(price)

        # Validate customer and coffee types
        from customer import Customer
        from coffee import Coffee
        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be a Coffee instance.")

        self._customer = customer
        self._coffee = coffee

        Order.all_orders.append(self)

    @property
    def price(self):
        # Price is read-only after creation
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee