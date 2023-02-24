"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
"""
def isPalindrome(num):
    if num < 0 or (num != 0 and num % 10 == 0):
        return False
#check if reversed num == num
    rev = 0
    n = num
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return n == rev
    
# Reverse the right half of the digits
# 6	    rev = 0
# 7	    while num > rev:
# 8	        rev = rev * 10 + num % 10
# 9	        num = num // 10
# 10	
# 11	    # Compare the reversed right half to the left half
# 12	    return num == rev or num == rev // 10

#print(isPalindrome(1234))

