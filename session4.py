import random
from decimal import *

class Qualean:
    '''
    Description: Qualean class is inspired by Boolean+Quantum concepts.
    We can assign it only 3 possible real states. 
    True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. 
    The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) 
    and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place.
    '''
    # the init function either takes the user's input or sets to default = ''.
    def __init__(self, user_input=""):
        if user_input and user_input not in [-1,0,1]: #checks if the user's input is valid
            raise ValueError("Invalid input: the user input should be [True, False or Maybe] or [-1,0,1].")
        elif user_input in [-1,0,1]: #if valid user's input.
            self.user_input=user_input
        else:                           # if no user's input then a random choice is made from [-1,0,1]
            self.user_input=random.choice([-1,0,1])
        self.number = round(float(Decimal((self.user_input*random.uniform(-1, 1)))),10) #storing the number in Qualean format.
    def return_qualean(self): # function returns the qualean number of the instance.
        return self.number
    def __bool__(self): #function returns the bool value of qualean.number.
        return True if self.number else False
    # defining object representation
    def __repr__(self):
        return 'Qualean Class Instance'
    def __str__(self): # defining the string representation of qualean class
        return ("Qualean String for number: " +str(self.number))
    def __invertsign__(self): #function returns the inverted value.
        return Decimal(self.number*-1)
    def __sqrt__(self): #function returns the square_root value
        if self.number>=0: #this is for positive numbers
            return round(Decimal(self.number**0.5),10)
        else: #this is for neagtive numbers. Here 'i' == sqrt(-1)
            return str(round(Decimal((-self.number)**0.5),10))+'i'
    def __float__(self): #function returns the float value
        return float(self.number)
    def __and__(self,other): #performs the "and" function
        result=other if self else self # logic of "and" is return x if x is False else y
        return bool(result) #result== either self or other, hence finding the bool of it.
    def __or__(self,other): #performs the "or" function 
        return True if other==None else bool(self if self else other) #logic of "or" is return x if x is True else y
    def __add__(self,other): #performs addition function
        if type(other)==str: #addition cannot be performed on "strings"
            raise TypeError("Invalid input")
        else: # checks if 'other' is an qualean or not.
            return self.number + other.number if type(self)==type(other) else float(self.number) + other
    def __mul__(self,other): #performs multiplication function
        if type(other)==str: #multiplication cannot be performed on "strings".
            raise TypeError("Invalid input")
        else:
            return self.number * other.number if type(self)==type(other) else float(self.number) * other
    #the following functions performs the standard operation
    #__ge__ as greater than or equal to
    #__gt__ as greater than
    #__le__ as less than or equal to
    #__lt__ as less than
    #__eq__ as equal to
    def __ge__(self,other):
        if type(other)==str:
            raise TypeError("Invalid input")
        else:
            return self.number >= other.number if type(self)==type(other) else float(self.number) >= other
    def __gt__(self,other):
        if type(other)==str:
            raise TypeError("Invalid input")
        else:
            return self.number > other.number if type(self)==type(other) else float(self.number) > other
    def __le__(self,other):
        if type(other)==str:
            raise TypeError("Invalid input")
        else:
            return self.number <= other.number if type(self)==type(other) else float(self.number) <= other
    def __lt__(self,other):
        if type(other)==str:
            raise TypeError("Invalid input")
        else:
            return self.number < other.number if type(self)==type(other) else float(self.number) < other
    def __eq__(self,other):
        if type(other)==str:
            raise TypeError("Invalid input")
        else:
            return self.number == other.number if type(self)==type(other) else float(self.number) == other