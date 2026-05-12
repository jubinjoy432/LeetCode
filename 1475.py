#Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        l=len(prices)
        if l==1 or l==0:
            return prices
        for i in range(l-1):
            j=i+1
            while prices[j]>prices[i] and j<l-1:
                j+=1
            if prices[j] <= prices[i]:
                ans.append(prices[i]-prices[j])
            else:
                ans.append(prices[i])
        ans.append(prices[-1])
        return ans
