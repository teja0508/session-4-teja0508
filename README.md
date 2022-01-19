# epai3session4
<h1 align="center">Numeric Types II</h1>

<h2 align="center"> Assignment Question </h2>


1. Write a Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. 
   1. It implements these functions (with exactly the same names)
      1. __and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__
2. Your task is to write the above class, and then write all the functions. 
3. Then you need to write a test file, that tests all of the functions mentioned above + the other basic ones you have seen in the tests till now. Your unit test file must contain at least 25 tests, and they must not be repetitive. Some of the tests it must implement are:
   1. q + q + q ... 100 times = 100 * q
   2. q.__sqrt__() = Decimal(q).sqrt
   3. sum of 1 million different qs is very close to zero (use isclose)
   4. q1 and q2 returns False when q2 is not defined as well and q1 is False
   5. q1 or q2 returns True when q2 is not defined as well and q1 is not false
4. Upload your code and your test file and make use of GitHub Actions and submit the GitHub link. 
5. No README, no evaluation. README must explain each function and each test case. 150 points for your code. 250 points for your test file

<h2 align="center"> Assignment Solution </h2>

Here we are given functions __and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__ and __bool__ to implement inside a class named Qualean which takes in an integer (either 1,0 or -1 ) and randimly selects a number from range -1 to 1 and multiplies to that number. Then the number is rounded off to 10th decimal digit. 
This Assignmented also required is to write minimum of 25 test cases but we wrote **34 test cases and implemented all functionalities**. 

### **Functions**

* #### **__init__ function**:

    Here the number selected from the user is passed as the paramter, it is generally of type Decimal. The choice of the user is then passed to number_transformation function which returns a value which is stored in self.value variable.

* #### **number_transformation function**:

    This function is called from the __init__ function. The choice of the user is passed as the parameter, it randomly selects a number between -1 and 1, converts to Decimal type, multiplied it with the choice of the user, rounded it off to 10th decimal place and returned back to __init__ function.

* #### **__and__ function**: 

    The task of this function is to perform and operation, it takes in other_object as parameter. If self.value is not zero, then it proceeds to check for the ottehr value else via shorthand returns False. While checking the other_other, it checks whether it is an object of class Qualean and is not zero, if any of the condiiton fails it returns False, else it performs an and operation and returns the result.

* #### **__or__function**:

    The task of this function is to perform or operation, it takes in other_object as parameter. If self.value is zero, then it proceeds to check for the ottehr value else via shorthand returns True. While checking the other_other, it checks whether it is an object of class Qualean and is not zero, if any of the condiiton fails it returns False, else it performs an or operation and returns the result.

* #### **__repr__ function**:

    Here we had to override this function, the task of this function is to return object represenation. Initially it was displaying the location of the object. Later we make it display the object and the user choice value.

* #### **__str__ function**:

    The task of this function is to return the string representation of the object. it is invoked when print() and str() is called. Initially is was also displaying the memory location of the object. Now is displaying the object and its user choice value.

* #### **__add__ function**:

    This function takes in value as a paramter, This value is added to the original value i.e. self.value and final result is returned back.

* #### **__eq__ function**:

    This function checks whether the numbers are equal or not. It takes in other number as paramter. The other number is compared with self. value number and the comparision result is returned i.e. True if they are equal else false. 

* #### **__float__ function**:

    This function has the task to convert the datatype of our value variable i.e. self.value, to float. The result is returned back.

* #### **__ge__ function**:

    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is greater than or equal to value. 

* #### **__gt__ function**:

    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is greater than value. 

* #### **__le__ function**:

    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is lesser than or equal to value. 

* #### **__lt__ function**:

    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is lesser than value. 

* #### **__invertsign__ function**:

    This function has the task to convert negative numbers postive and positive numbers negative. Once the conversion is done it returns the value

* #### **__mul__ function**:

    This function is similar as __add__ function, here the value parameter is multiplied with self.value and the result is returned back.

* #### **__sqrt__ function**:

    This function has the task to get the square root of the number. If self.value number is negative, it converts the number to postive, performs the square root and returns the result with an 'i' added in the result. Whereas if the number is positive, it follows the same process where as i is not added here. The result directly is returned back.

* #### **__bool__ function**:

    This function is used to convert the self.value variable to boolean value
