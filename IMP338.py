#Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            ans.append(bin(i).count("1"))
        return ans
###########or###################
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            count=0
            n=i
            while n!=0:
                if n%2==1:
                    count+=1
                n//=2
            ans.append(count)
        return ans
######################3or###################
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]
        for i in range(1,n+1):
            ans.append(ans[i>>1]+i%2)
        return ans