'''
Best Time to Buy and Sell Stock II 

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).	


'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        change = []
        for i in range(0, len(prices) - 1):
            change.append( prices[i+1] - prices[i])
        
        sum = 0
        for i in change:
            if i > 0:
                sum += i
        
        return sum

a =Solution()

print a.maxProfit([10,7,8,9,4,10])