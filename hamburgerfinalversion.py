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

        

# Dictionary to store customers and their burger counts
customer_dict = {}

# Queue to hold the customers
customer_queue = []




# Generating 100 random customers
for chosenCustomer in range(100):
    customer = Customer(customer_dict)
    customer_queue.append(customer.name)

    if customer.name in customer_dict:
        customer_dict[customer.name] += customer.burger_count
    else:
        customer_dict[customer.name] = customer.burger_count

# Printing customer names and their corresponding burger counts
listSortedCustomers = sorted(customer_dict.items(), key=lambda x: x[1], reverse=True) 
for iCount in range(0, len(listSortedCustomers)) :
    print(listSortedCustomers[iCount][0].ljust(19), listSortedCustomers[iCount][1])
    customer_queue.pop(0)
