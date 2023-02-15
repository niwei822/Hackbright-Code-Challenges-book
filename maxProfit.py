def maxProfit(lst):
    max_price = 0
    min_price = lst[0]
    for i in range(1, len(lst)):
        max_price = max((lst[i] - min_price), max_price)
        min_price = min(min_price, lst[i])
    return max_price
print(maxProfit([7,6,4,3,1]))
        
