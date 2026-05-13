#Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=len(cost)
        dp=[0 for i in range(l)]
        dp[l-1]=cost[l-1]
        for i in range(l-2,-1,-1):
            if i+1==l-1:
                dp[i]=cost[i]
            else:
                dp[i]=cost[i]+min(dp[i+1],dp[i+2])
        return min(dp[0],dp[1])