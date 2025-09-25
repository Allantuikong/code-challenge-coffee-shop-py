# Coffee Shop Code Challenge

This project is a simple object-oriented Python application that models a coffee shop system. It demonstrates the use of classes, properties, and relationships between customers, coffees, and orders.

## Features

- **Customer**: Represents a customer with a validated name. Customers can create orders and view their coffees.
- **Coffee**: Represents a coffee type with a unique, immutable name. Tracks all orders and customers for each coffee.
- **Order**: Represents an order linking a customer and a coffee, with a validated price.

## File Structure

- `customer.py` — Customer class and related logic
- `coffee.py` — Coffee class and related logic
- `order.py` — Order class and related logic
- `tests/` — Contains test files (e.g., `test_coffee.py`)

## Getting Started

1. **Clone the repository** and navigate to the project folder.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. **Install dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the code** by importing the classes in a Python shell or script.
5. **Run tests** (if available):
   ```bash
   pytest tests/
   ```

## Example Usage

```python
from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
coffee1 = Coffee("Latte")
order1 = Order(c1, coffee1, 3.5)
order2 = c2.create_order(coffee1, 4.0)
```

## Notes

- Names and prices are validated for correctness.
- Orders link customers and coffees.
- See each class for more details on available methods.

---

_This project is for educational purposes and code challenge practice._
