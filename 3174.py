#Clear Digits
class Solution(object):
    def clearDigits(self, s):
        stack=[]
        for i in s:
            if stack:
                if i.isdigit():
                    stack.pop()
                else:
                    stack.append(i)
            else:
                    stack.append(i)
        return "".join(stack)
        