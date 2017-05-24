import math
from math import *

def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print ("%d squared is %d." % (n, squared))
    return squared

def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print ("%d to the power of %d is %d." % (base, exponent, result))



# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)
power(37,4)  # Add your arguments here!

#=========================================================
def cube(number):
    return number * number * number


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

#=========================================================
print (sqrt(25))
everithing = dir(math)
print (everithing)

#==========================================================
def biggest_number(*args):
    print (max(args))
    return max(args)


def smallest_number(*args):
    print (min(args))
    return min(args)


def distance_from_zero(arg):
    print (abs(arg))
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#==============================================================
print (type (21))
print (type (21.2))
print (type ('dawdaww'))