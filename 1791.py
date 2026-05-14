#Find Center of Star Graph
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c=[]
        for e in edges:
            if e[0] in c:
                return e[0]
            c.append(e[0])
            if e[1] in c:
                return e[1]
            c.append(e[1])