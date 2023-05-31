# Group 7- Authors: Eli Baker, Cayden Eastman, Mckay Lush, Chase Hindmarsh, Cooper Burden, Gavin Smith
# Description: A program that generates customers and their orders and adds them to a keylisted dictionary and outputs them in descending order of burgers


# importing random function and importing a way to queue the customers
import random
from collections import deque

# A class that generates a random amount of burgers between 1-20 each time they order
class Order:
    def __init__(self):
        self.burger_count = random.randint(1, 20)

# Creates a class that lists the 9 customers and will randomly choose them 
class Person:
    def __init__(self):
        self.name = self.randomName()

    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

    
# Creates a child class to the person class and calls the the Person class and creates a variabole called order that is an instance of the class "Order"
class Customer(Person):
    def __init__(self, customer_dict):
        super().__init__()
        self.order = Order()
        self.burger_count = self.order.burger_count

        

# Dictionary to store customers and their burger counts
customer_dict = {}

# Queue to hold the customers
customer_queue = []


# Choosing the customers 100 times and adding their name and burger count to a dictionary. If their name doesnt exist in the dictionary, it will add both name and 
# burger count, if it does exist already it will add to their existing burger count. 
for chosenCustomer in range(100):
    customer = Customer(customer_dict)
    customer_queue.append(customer.name)

    if customer.name in customer_dict:
        customer_dict[customer.name] += customer.burger_count
    else:
        customer_dict[customer.name] = customer.burger_count

        
# Printing customer names and their corresponding burger counts in descending order in the format that was required. Pops the customer out of the queue. 
listSortedCustomers = sorted(customer_dict.items(), key=lambda x: x[1], reverse=True) 
for iCount in range(0, len(listSortedCustomers)) :
    print(listSortedCustomers[iCount][0].ljust(19), listSortedCustomers[iCount][1])
    customer_queue.pop(0)
