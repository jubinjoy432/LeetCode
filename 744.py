#Find Smallest Letter Greater Than Target
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        r=len(letters)-1
        while l<=r:
            mid=(l+r)//2
            if letters[mid]>target:
                if letters[mid-1]<=target:
                    return letters[mid]
                else:
                    r=mid-1
            else:
                l=mid+1
        return letters[0]