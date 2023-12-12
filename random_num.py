'''
print 5 random numbers 

'''

import random

def rand_num():
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    print("5 lottery Random Numbers:", random_numbers)
    

if __name__ == "__main__": 
    rand_num()
