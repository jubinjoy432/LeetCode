#Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        rom={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans=0
        l=len(s)-1
        for i in range(l,-1,-1):
            if s[i] in "IXC":
                if i!=l:
                    if s[i]=="I" and s[i+1] in "VX":
                        ans-=1
                        continue
                    elif s[i]=="X" and s[i+1] in "LC":
                        ans-=10
                        continue
                    elif s[i]=="C" and s[i+1] in "DM":
                        ans-=100
                        continue
            ans+=rom[s[i]]
        return ans