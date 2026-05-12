#plus one
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=0
        l=len(digits)-1
        digits[l]+=1
        for i in range(l,-1,-1):
            if c==1:
                digits[i]+=c
                c=0
            if digits[i]>9:
                digits[i]=0
                c=1
        if c==1:
            digits.insert(0,1)
        return digits