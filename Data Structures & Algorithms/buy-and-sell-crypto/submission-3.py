class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        max_profit = 0
        i = 0
        j = 1

        while j < len(prices):
            
            profit = prices[j] - prices[i]

            if profit < 0:
                i=j
            if profit > 0:
                if profit > max_profit:
                    max_profit = profit
            j += 1

        return max_profit


        