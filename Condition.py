# Set this to True if 17 < 328 or to False if it is not.
bool_one = 17 < 328
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = 100 == (2 * 50)
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = 19 <= 19
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = -22 >= -18
bool_four =  False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = 99 != (98 +1)
bool_five = False

#=======================Operator And===============================

# 40 * 4 >= -4
bool_four = 40 * 4 >= -4

# 100 != 10**2
bool_five = 100 != 10 **2

bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5

bool_three = 19 % 4 != 300 /10/10 and False

bool_four = -(1**2) < 2**0 and 10 %10 <= 20 -10 *2

bool_five = True and True

print (bool_one)
print (bool_two)
print (bool_three)
print (bool_five)

#====================Operator Or======================================

bool_six = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_seven = True or False

bool_eight = 100**0.5 >= 50 or False

bool_nine = True or True

bool_ten = 1**100 == 100** 1 or 3 * 2 * 1 != 3 + 2 + 1

print (bool_six)
print (bool_seven)
print (bool_eight)
print (bool_nine)
print (bool_ten)

#====================not=================================
bool_one_not = not True

bool_two_not = not 3**4 < 4**3

bool_three_not = not 10%3 <= 10%2

bool_four_not = not 3**2 + 4**2 !=5**2

bool_five_not = not not False

print (bool_one_not)
print (bool_two_not)
print (bool_three_not)
print (bool_four_not)
print (bool_five_not)