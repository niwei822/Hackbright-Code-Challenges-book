def plusOne(digits):
    i = len(digits) - 1
    digits[i] += 1
    if digits[i] <= 9:
        return digits
    while i > 0 and digits[i] == 10:
        digits[i] = 0
        digits[i-1] += 1
        i -= 1
    if digits[0] == 10:
        digits[0] = 0
        digits.insert(0, 1)
    return digits
            
print(plusOne([1,8,9,9]))