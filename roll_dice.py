from random import randint

def roll_dice():
    return randint(1,6)

# print(roll_dice())
    
def dice_shape(number): 
    if number == 1:
        return """
        ===========
        |         |
        |    0    |
        |         |
        ===========
        """  
    elif number == 2:
        return """
        ===========
        |      0  |
        |         |
        | 0       |
        =========== 
        """
    elif number == 3:
        return """
        ===========
        |       0 |
        |    0    |
        | 0       |
        =========== 
"""
    elif number == 4:
        return """
        ===========
        | 0     0 |
        |         |
        | 0     0 |
        ===========
"""
    elif number == 5:
        return """
        ===========
        | 0     0 |
        |    0    |
        | 0     0 |
        ===========

"""
    elif number == 6:
        return """
        ===========
        | 0     0 |
        | 0     0 |
        | 0     0 |
        ===========
    
"""
    else :
        return "error"
    
#print(dice_shape())

def dice():


    
    return dice_shape(roll_dice())

print(dice())