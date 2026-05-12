#Separate the Digits in an Array
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s="".join(map(str,nums))
        ans=list(map(int,s))
        return ans