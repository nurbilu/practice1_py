'''
print 5 random numbers 

'''
from icecream import ic 
import random

def rand_num():
    random_numbers = [random.randint(1, 41) for _ in range(5)]
    ic("5 lottery Random Numbers:", random_numbers)
    

if __name__ == "__main__": 
    ic.disable()
    rand_num()
    ic.enable()
    rand_num()
