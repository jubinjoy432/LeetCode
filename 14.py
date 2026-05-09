#Longest Common prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0]=="":
            return ""
        i=0
        subs=""
        c=strs[0][0]
        flag=True
        while flag==True:
            for s in strs:
                if i==len(s):
                    flag=False
                elif s[i]!=c:
                    flag=False
            if flag==True:
                subs=subs+c
            i+=1
            if len(strs[0])==i:
                flag=False
                break
            c=strs[0][i]
        return subs