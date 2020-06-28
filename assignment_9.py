"""
Assignment #9 by
   Sandy Nguyen
   06/15/2020
   "An Order of Sandwiches" Program

Program description: This program uses the class of Sandwich from assignment #5 by first initializing a
single sandwich object by storing its name as an instance variable and then setting the additional ingredients
to contain values in parameters. Once these are defined, the program will check through a series of if statements
and iterate through the list (and additional condiments if they are appended) to see if they are True, and
if so to add them to the string of s. The program will do the same thing but with the intent of finding
the price, given that the standard price is $4.50.
"""


class Sandwich:
    # One object of this class represents a person's sandwich order. each object represents a sandwich in which it has
    # instances that make up the sandwich
    def __init__(self, name):
        # Initializes a single new Sandwich object by storing the name as its instance variable name.
        self._name = name
        self._bread = None
        self._cheese = None
        self._meat = None
        self._condiments = []
        self._toasted = False

    def setBread(self, breadName):
        # Sets the bread instance variable to contain the value in the parameter "breadName".
        self._bread = breadName

    def setCheese(self, cheeseName):
        # Sets the cheese instance variable to contain the value in the parameter "cheeseName".
        self._cheese = cheeseName

    def setMeat(self, meatName):
        # Sets the meat instance variable to contain the value in the parameter "meatName".
        self._meat = meatName

    def addCondiment(self, additionalCondiment):
        # Adds "additionalCondiment" to the list of condiments stored in the instance variable for the condiments list.
        self._condiments.append(additionalCondiment)

    def setToasted(self, isToasted):
        # Sets the toasted instance variable to be True if the parameter "isToasted" is True, False otherwise.
        self._toasted = isToasted

    def __str__(self):
        # Returns a string containing the description of the sandwich which includes a list of all the ingredients.
        s = self._name + ": "
        if self._bread:
            s += self._bread + ", "
        if self._cheese:
            s += self._cheese + ", "
        if self._meat:
            s += self._meat + ", "
        if self._condiments:
            s += str(self._condiments) + ", "
        if self._toasted:
            s += "toasted"
        else:
            s += "not toasted"
        return s

    def price(self):
        # Returns the price of the sandwich based on the price list.
        p = 4.5

        if self._meat:
            p += 1

        p += (len(self._condiments) - 1) * 0.5

        return p

