'''
Given an array prices, which represents the price of a stock in each day.

You may complete as many transactions as you like (ie, buy one and sell one
share of the stock multiple times). However, you may not engage in multiple 
transactions at the same time (ie, if you already have the stock, you must 
sell it before you buy again).
'''
def max_profit(prices):
    max_profit = 0
    if not prices:
        return 0
    for i in range(0, len(prices)-1):
        if prices[i+1] > prices[i]:
            max_profit += prices[i+1] - prices[i]
    return max_profit
            
       