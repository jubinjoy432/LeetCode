#Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pas=[[1]]
        for i in range(1,rowIndex+1):
            r=[]
            for j in range(i+1):
                if j==0 or j==i:
                    r.append(1)
                else:
                    r.append(pas[i-1][j-1]+pas[i-1][j])
            pas.append(r)
        return pas[rowIndex]