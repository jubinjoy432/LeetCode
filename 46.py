#Last Stone Weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                x=stones[-1]-stones[-2]
                stones.pop()
                stones[-1]=x
                stones.sort()
        if stones:
            return stones.pop()
        else:
            return 0