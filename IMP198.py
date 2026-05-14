#House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        elif len(nums)==1:
            return nums[0]
        else:
            ans=[0]*len(nums)
            ans[0]=nums[0]
            ans[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                ans[i]=max(ans[i-2]+nums[i],ans[i-1])
            return ans[-1]
