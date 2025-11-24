'''
merge sort,stable and fast sort but use more Ram space.
'''
import random

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

test_array = [8,5,3,9,11,17,4,26,10,7]
print("sorted array =", merge_sort(test_array))