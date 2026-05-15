#Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        minimum=prices[0]
        profit=0
        for i in range(1,l):
            minimum=min(minimum,prices[i])
            profit=max(profit,prices[i]-minimum)
        return profit