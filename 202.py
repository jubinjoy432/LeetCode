#happy number
class Solution:
    def isHappy(self, n: int) -> bool:
        prev=[]
        while n!=1:
            s=0
            while n>0:
                i=n%10
                s+=(i*i)
                n=n//10
            if s in prev:
                return False
            prev.append(s)
            n=s
        return True
#########################or#######################################
def isHappy(self, n: int) -> bool:
        count=0
        while n!=1:
            sum=0
            while n>0:
                i=n%10
                sum+=(i*i)
                n=n//10
            count+=1
            if count>10:
                return False
            n=sum
        return True