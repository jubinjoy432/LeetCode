#sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        prev=0
        if x==1 or x==0:
            return x
        for i in range((x//2)+2):
            sq=i*i
            if sq==x:
                return i
            elif sq<x:
                prev=i
            elif sq>x:
                return prev