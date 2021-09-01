#import this

"""import math 

x = math.sqrt(9) #sqrt is a method that finds the squareroot
print(x)

y = math.ceil(x) #ceil method rounds of the number to a whole number
print(y)"""

from math import sqrt, ceil #from keyword allows us to use the method name directly without referencing the module

x = sqrt(9)
print(x)

y = ceil(x)
print(y)

import random #random module 
#randint method is used to generate a random number
# randint parameters define the range of values from which python will choose a random number
def new_func():
    random_number = random.randint(0,10)
    return random_number

random_number = new_func()
print(random_number)
