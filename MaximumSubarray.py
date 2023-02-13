def maxSubArray(nums):
    """Given an integer array nums, find the subarray
        with the largest sum, and return its sum.
    """
    max_sum = nums[0]
    sub_sum = 0
    for num in nums:
        if sub_sum < 0:
            sub_sum = 0
        sub_sum += num
        max_sum = max(max_sum, sub_sum)
    return max_sum
#print(maxSubArray([-2,-1,-3,-4,-1,-2,-1,-5,-4]))