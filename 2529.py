#Maximum Count of Positive Integer and Negative Integer
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        length=len(nums)
        if nums[0]>0 or nums[-1]<0:
            return length
        elif nums[0]==0 or nums[-1]==0:
            return length-nums.count(0)
        l=0
        r=length-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=0:
                if nums[mid-1]<0:
                    return max(mid,length-mid-nums.count(0))
                else:
                    r=mid-1
            else:
                l=mid+1