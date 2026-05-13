#Fibonacci number
class Solution:
    def fib(self, n: int) -> int:
        dp=[0,1]
        if n==0 or n==1:
            return dp[n]
        for i in range(2,n+1):
            dp.append(dp[-1]+dp[-2])
        return dp[-1]
#######################or#######################3
class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)