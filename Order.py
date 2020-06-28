"""
Assignment #9 by
   Sandy Nguyen
   06/15/2020
   "An Order of Sandwiches" Program

Program description: This program uses the Sandwich class and creates a class called Order. It then initializes an order
which represents an order of multiple sandwiches to be made at the deli. It then adds these sandwiches to a list
and appends them together. The total price is found by looping through every Sandwich in the order list and adds them
up. The str method appends the object to each person's order (for ex. Joe).
"""


from assignment_9 import Sandwich


class Order:
    #One object of class Order represents a whole Order consisting of multiple Sandwiches to be made at the deli.
    def __init__(self):
    #Initializes an empty order object.
        self.order = []

    def addSandwich(self, newSandwich):
    #Adds new Sandwich to the order.
        self.order.append(newSandwich)

    def price(self):
    #Returns the total price of all the sandwiches in the order.
        price = 0
        for sandwich in self.order:
            price += sandwich.price()
        return price

    def __str__(self):
    #Returns a string containing the names and contents of all the Sandwiches in the Order.
        if len(self.order) != 0:
            s = f"Sandwich #1: {str(self.order[0])}"
            for sandwich in range(1, len(self.order)):
                s += f"\nSandwich #{sandwich+1}: {str(self.order[sandwich])}"
            return s

        else:
            return "No sandwiches in the order."





