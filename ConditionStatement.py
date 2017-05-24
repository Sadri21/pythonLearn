def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print (using_control_once())
print (using_control_again())

#==========================================
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0


print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))
#=====================================

def the_flying_circus():
    if 3 < 2:  # Start coding here!
        return False
    elif (4 > 3) and (5 < 3):
        return False
        # You'll want to add the else statement, too!
    else:
        return True


print(the_flying_circus())