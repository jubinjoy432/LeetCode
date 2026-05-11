#3sum closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        length=len(nums)
        for i in range(0,length):
            l=i+1
            r=length-1
            while l<r:
                sum=0
                sum=nums[i]+nums[l]+nums[r]
                if sum==target:
                    return sum
                elif sum>target:
                    r-=1
                else:
                    l+=1
                if abs(target-sum)<=abs(target-res):
                    res=sum
        return res