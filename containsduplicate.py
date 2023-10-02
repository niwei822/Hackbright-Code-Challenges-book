'''
Given an array of integers, find if the array contains any 
duplicates. Your function should return true if any value 
appears at least twice in the array, and it should return 
false if every element is distinct.
'''

def contains_duplicate(nums):
    return len(set(nums)) != len(nums)

print(contains_duplicate([1, 2, 3]))