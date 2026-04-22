#Minimum String Length After Removing Substrings
class Solution(object):
    def minLength(self, s):
        stack=[]
        c="AC"
        d="BD"
        for i in s:
            if stack:
                if stack[-1]=="A" and i=="B" or stack[-1]=="C" and i=="D":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                    stack.append(i)
        return len(stack)