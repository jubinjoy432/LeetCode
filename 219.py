#contains duplicate 2
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s={}
        for i in range(len(nums)):
            if nums[i] not in s:
                s[nums[i]]=i
            elif nums[i] in s and abs(i-s[nums[i]])<=k:
                return True
            else:
                s[nums[i]]=i
        return False