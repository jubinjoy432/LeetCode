#Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        if numRows==1:
            return ans
        for i in range(1,numRows):
            r=[]
            for j in range(i+1):
                if j==0 or j==i:
                    r.append(1)
                else:
                    r.append(ans[i-1][j-1]+ans[i-1][j])
            ans.append(r)
        return ans
