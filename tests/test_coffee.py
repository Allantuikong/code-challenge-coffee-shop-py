import pytest

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def test_customer_creation():
    customer = Customer("Alice", 30)
    assert customer.name == "Alice"
    assert customer.age == 30