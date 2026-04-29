#shortest distance to target string in a circular array
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex]==target:
            return 0
        l=len(words)
        i=(startIndex+1)%l
        j=(startIndex-1+l)%l
        fcount=1
        bcount=1
        while i!=startIndex and j!=startIndex:
            if words[i]==target:
                return fcount
            elif words[j]==target:
                return bcount
            i=(i+1)%l
            fcount+=1
            j=(j-1+l)%l
            bcount+=1
        return -1