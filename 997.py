#Find the Town Judge
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        j=[]
        p=[]
        c={}
        if n==1 and not trust:
            return 1
        for i in trust:
            p.append(i[0])
            if i[1] not in j:
                c[i[1]]=1
                j.append(i[1])
            else:
                c[i[1]]+=1
        for i in p:
            if i in j:
                j.remove(i)
        if j and c[j[0]]==n-1:
            return j[0]
        else:
            return -1