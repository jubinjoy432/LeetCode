#power of 4
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x=n
        count=0
        while x>0:
            x=x>>1
            count+=1
        if n&(n-1)==0 and (count-1)%2==0:
            return True
        else:
            return False