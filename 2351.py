#First Letter to Appear Twice
class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for i in s:
            if i in st:
                return i
            else:
                st.append(i)
