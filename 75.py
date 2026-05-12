#Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count={0:0,1:0,2:0}
        for i in nums:
            count[i]+=1
        i=0
        l=count[0]
        while i<l:
            nums[i]=0
            i+=1
        l=i+count[1]
        while i<l:
            nums[i]=1
            i+=1
        l=i+count[2]
        while i<l:
            nums[i]=2
            i+=1