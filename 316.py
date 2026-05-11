#Remove Duplicate Letters
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c=list(s)
        st=[]
        for i in s:
            if c:
                c.pop(0)
            if i not in st:
                while st and i<st[-1] and st[-1] in c:
                    st.pop()
                st.append(i)
                
        return "".join(st)