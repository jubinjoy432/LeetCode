#Sum of Values at Indices With K Set Bits
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans=[0]
        sum=0
        for i in range(1,len(nums)):
            ans.append(ans[i>>1]+i%2)
        for i in range(len(nums)):
            if ans[i]==k:
                sum+=nums[i]
        return sum