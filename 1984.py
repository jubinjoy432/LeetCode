#min diff bw high and low of k scores
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l=len(nums)
        if l==1:
            return 0
        l=len(nums)
        nums.sort()
        s=[]
        m=max(nums)
        for i in range(l-k+1):
            d=nums[i+k-1]-nums[i]
            m=min(m,d)
        return m