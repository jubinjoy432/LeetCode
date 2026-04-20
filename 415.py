#Add Srings
class Solution(object):
    def addStrings(self, num1, num2):
        c=0
        l1=len(num1)-1
        l2=len(num2)-1
        sum=""
        while l1>=0 or l2>=0:
            if l1<0:
                x=0
                y=int(num2[l2])
            elif l2<0:
                x=int(num1[l1])
                y=0
            else:
                x=int(num1[l1])
                y=int(num2[l2])
            a=x+y+c
            c=0
            if a>9:
                c=1
                sum=str(a-10)+sum
            else:
                sum=str(a)+sum
            l1-=1
            l2-=1
        if l1>=0:
            while l1>=0:
                sum=num1[l1]+sum
                l1-=1
        if l2>=0:
            while l2>=0:
                sum=num2[l2]+sum
                l2-=1
        if c==1:
            sum=str(c)+sum
        return sum


                
        