#Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=Counter(s)
        b=Counter(t)
        for i in b:
            if a[i]!=b[i]:
                return i