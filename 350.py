#Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res=[]
        p1=p2=0
        l1=len(nums1)
        l2=len(nums2)
        while p1<l1 and p2<l2:
            if nums1[p1]==nums2[p2]:
                res.append(nums1[p1])
                p1+=1
                p2+=1
            elif nums1[p1]<nums2[p2]:
                p1+=1
            else:
                p2+=1
        return res