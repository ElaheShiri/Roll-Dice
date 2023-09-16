from random import randint
    
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

def dice():
    return dice_shape(randint(1,6))

print(dice())