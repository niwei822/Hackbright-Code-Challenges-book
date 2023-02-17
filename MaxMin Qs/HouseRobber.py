"""looking for the maximum sum of non-adjacent elements. """
def rob(nums):
    prev = 0
    curr = 0
    for num in nums:
        temp = curr
        curr = max(prev + num, curr)
        prev = temp
    return curr

print(rob([2,1,1,2]))