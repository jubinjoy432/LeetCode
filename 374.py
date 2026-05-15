#Guess Number Higher or Lower
class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        r=n
        while l<=n:
            mid=(l+r)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res>0:
                l=mid+1
            else:
                r=mid-1