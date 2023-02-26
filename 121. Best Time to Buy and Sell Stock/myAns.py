class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        getPrice = prices[0]
        profit = 0
        for i in prices:
            if i - getPrice > profit:
                profit = i - getPrice
            if i < getPrice:
                getPrice = i

        return profit
            
