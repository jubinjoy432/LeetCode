#N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        t=[0,1,1]
        if n==0 or n==1 or n==2:
            return t[n]
        for i in range(3,n+1):
            t.append(t[-1]+t[-2]+t[-3])
        return t[-1]