import random
from collections import deque

class Order:
    def __init__(self):
        self.burger_count = random.randint(1, 20)

class Person:
    def __init__(self):
        self.name = self.randomName()

    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

class Customer(Person):
    def __init__(self, customer_dict):
        super().__init__()
        self.order = Order()
        self.burger_count = self.order.burger_count

        if self.name in customer_dict:
            customer_dict[self.name] += self.burger_count
        else:
            customer_dict[self.name] = self.burger_count

# Dictionary to store customers and their burger counts
customer_dict = {}

# Queue to hold the customers
customer_queue = deque()

# Generating 100 random customers
for chosenCustomer in range(100):
    customer = Customer(customer_dict)
    customer_queue.append(customer)

# Printing customer names and their corresponding burger counts
sorted(customer_dict)
for name, burger_count in customer_dict.items():
    print(f'{name}: {burger_count} burgers')