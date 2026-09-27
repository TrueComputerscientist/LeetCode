class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = float('inf')
        mostProfit = float('-inf')
        for price in prices:
            if price < lowest:
                lowest = price
            profit = price - lowest
            if profit > mostProfit:
                mostProfit = profit
        if mostProfit > 0:
            return mostProfit
        else:
            return 0