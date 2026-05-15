#Baseball Game
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        x=0
        for i in operations:
            if i=="+":
                b=s[-1]
                a=s[-2]
                s.append(a+b)
            elif i=="D":
                s.append(s[-1]*2)
            elif i=="C":
                s.pop()
            else:
                s.append(int(i))
        for i in s:
            x+=i
        return x
        