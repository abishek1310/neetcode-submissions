class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_price = float('inf')
        max_profit = 0
        for i in prices:
            if i < low_price:
                low_price = i
            profit = i - low_price 
            if profit > max_profit:
                max_profit = profit
            else:
                max_profit = max_profit
        return max_profit 
        