def mySqrt(x):
    if x == 0 or x == 1:
        return x
    #start with the range of possible integer square roots of x
    # which is [0, x].
    max = x
    min = 0
    middle = (min + max)//2
    while (min < max):
        #computes the square of the middle element
        result = middle * middle
        if result == x:
            return middle
        #If the square of middle is less than x, then the integer square root 
        # of x must be in the range [middle+1, max].
        elif result < x:
            min = middle + 1
        else:
            #Otherwise, the integer square root of x must be in the range 
            # [min, middle-1]
            max = middle
        middle = (min + max)//2
    return middle - 1
print(mySqrt(10))
            