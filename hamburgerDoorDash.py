#Authors: Eli Baker, Cayden Eastman, Mckay Lush, Chase Hindmarsh, Cooper Burden, Gavin Smith
#Description: a program that generates customers and their orders and adds them to a keylisted dictionary

#importing random class
import random

#import a way to make a queue for customers
from collections import deque

#create a class that generates a set amount of burgers ordered for each customer everytime it is called
class Order:
    
    #generates a random number of burgers ordered
    def randomBurgers(self):
        return random.randint(1, 20)

    #assigns burger amounts to a variable
    def __init__(self):
        self.burger_count = self.randomBurgers()
    
#creates a parent class of attributes choosing between 9 different names and assigning that name to a variable
class Person():
    
    def randomName(self):
        lstCustomer_name = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(lstCustomer_name)
    
    def __init__(self):
        self.customer_name = self.randomName()

#creates a child class that calls the Person class and creates a variable called order that is an instance the class "Order"
class Customer(Person):
    
    def __init__(self):
        super().__init__
        self.order = Order()

#creates an empty queue
queue = deque()

#creates a for loop that adds a customer name and order amount to 100 different instances of the customer class
for iCustomer in range(100):
    queue.append(Customer())

#creates an empty dictionary that will be used to store customer data
dictCustomerInfo = {}

#creates a while loop that basically says that while there are customers in the queue, one will be popped out, assigned a name and an amount of burgers
while queue:
    iCustomer = queue.popleft()
    sCustomerName = Customer.customer_name
    iBurgersOrdered = Customer.Order.burger_count

    #this adds the customer info into the class with a key as the name and an integer as the burger count
    dictCustomerInfo [sCustomerName] = iBurgersOrdered