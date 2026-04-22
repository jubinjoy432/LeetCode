#Make The String Great
class Solution(object):
    def makeGood(self, s):
        stack=[]
        for i in s:
            if stack and lower(stack[-1])==lower(i):
                if stack[-1].isupper() and i.islower() or i.isupper() and stack[-1].islower():
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return "".join(stack)