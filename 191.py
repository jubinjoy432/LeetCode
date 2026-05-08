#bit 1 count
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
    
###################or########################

class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            n&=(n-1)
            res+=1
        return res