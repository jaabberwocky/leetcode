class Solution:
    def maxProfit(self, prices):
        if len(prices) < 1:
            return 0
        maxProfit, minPrice = 0, float('inf')
        for price in prices:
            if price < minPrice:
                minPrice = min(minPrice, price)
            else:
                profit = price - minPrice
                maxProfit = max(maxProfit, profit)
        return maxProfit