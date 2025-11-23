'''
quick sort algorithm for learning how does it work
'''
import random

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    random_number = random.choice(array)
    
    lower = [i for i in array if i < random_number]
    equal = [i for i in array if i == random_number]
    higher = [i for i in array if i > random_number]
    
    return quick_sort(lower) + equal + quick_sort(higher)

test_array = [3,25,10,7,64,13,58,19,21,34,1,2,8,9]
print(quick_sort(test_array))