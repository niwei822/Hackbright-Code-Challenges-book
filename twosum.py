"""
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the
same element twice. You can return the answer in any order.
"""
def two_sum(nums, target):
    """return index of two number"""
    result = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in result:
            return [result[diff], index]
        result[num] = index
    
print(two_sum([2,3,4], 5))
    