#defuse the bomb
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        dec=[]
        l=len(code)
        for i in range(l):
            if k>0:
                sum=0
                for j in range(1,k+1):
                    sum=sum+code[(i+j)%l]
                dec.append(sum)
            elif k<0:
                sum=0
                for j in range(1,abs(k)+1):
                    ind=i-j
                    if ind<0:
                        ind=l+ind
                    sum=sum+code[ind]
                dec.append(sum)
            else:
                dec.append(0)
        return dec