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

from Order import Order
from assignment_9 import Sandwich

if __name__ == "__main__":
    # sample test case
    s1 = Sandwich("Joe")
    s1.setMeat("steak")
    s1.addCondiment("Lettuce")
    print(s1)

    s2 = Sandwich("Mary")
    s2.setCheese("cheddar")
    s2.addCondiment("Mayo")
    print(s2)

    order = Order()
    print(order)
    order.addSandwich(s1)
    print(order)
    print("Total Price: " + str(order.price()))
    order.addSandwich(s2)
    print(order)
    print("Total Price: " + str(order.price()))

    print()
    print()
    # test case #2
    s3 = Sandwich("Jim")
    s3.setMeat("turkey")
    s3.addCondiment("Lettuce")
    print(s3)

    s4 = Sandwich("Sandy")
    s4.setMeat("Ham")
    s4.addCondiment("Mustard")
    print(s4)

    order2 = Order()
    print(order2)
    order2.addSandwich(s3)
    order2.addSandwich(s4)
    print(order2)
    print("Total Price: " + str(order2.price()))

    # showing that adding sandwich won't affect first order
    s5 = Sandwich("Kal")
    s5.setMeat("Ham")
    order2.addSandwich(s5)
    print("\nFirst order")
    print(order)
    print("Total Price: " + str(order.price()))
    print("\nSecond order")
    print(order2)
    print("Total Price: " + str(order2.price()))

    # another instance of order
    print("\nThird order")
    order3 = Order()
    print(order3)
    print("Total Price: " + str(order3.price()))
    s6 = Sandwich("Tim")
    s6.setMeat("Turkey")
    s6.addCondiment("Mustard")
    s6.setCheese("American")
    s6.setToasted(True)
    order3.addSandwich(s6)
    # price after new sandwich
    print(order3)
    print("Total Price: " + str(order3.price()))



"""
/Users/sandynguyen/PycharmProjects/assignment_9/venv/bin/python "/Users/sandynguyen/PycharmProjects/assignment_9/main program.py"
Joe: steak, ['Lettuce'], not toasted
Mary: cheddar, ['Mayo'], not toasted
No sandwiches in the order.
Sandwich #1: Joe: steak, ['Lettuce'], not toasted
Total Price: 5.5
Sandwich #1: Joe: steak, ['Lettuce'], not toasted
Sandwich #2: Mary: cheddar, ['Mayo'], not toasted
Total Price: 10.0


Jim: turkey, ['Lettuce'], not toasted
Sandy: Ham, ['Mustard'], not toasted
No sandwiches in the order.
Sandwich #1: Jim: turkey, ['Lettuce'], not toasted
Sandwich #2: Sandy: Ham, ['Mustard'], not toasted
Total Price: 11.0

First order
Sandwich #1: Joe: steak, ['Lettuce'], not toasted
Sandwich #2: Mary: cheddar, ['Mayo'], not toasted
Total Price: 10.0

Second order
Sandwich #1: Jim: turkey, ['Lettuce'], not toasted
Sandwich #2: Sandy: Ham, ['Mustard'], not toasted
Sandwich #3: Kal: Ham, not toasted
Total Price: 16.0

Third order
No sandwiches in the order.
Total Price: 0
Sandwich #1: Tim: American, Turkey, ['Mustard'], toasted
Total Price: 5.5

Process finished with exit code 0

"""










