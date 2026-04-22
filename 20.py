#Valid Parentheses
class Solution(object):
    def isValid(self, s):
        stack=[]
        open="{[("
        close="}])"
        flag=0
        for i in s:
            if i in open:
                stack.append(i)
                flag+=1
            elif i in close and len(stack)!=0:
                if i==")":
                    x=stack.pop()
                    if x=="(":
                        flag-=1
                if i=="}":
                    x=stack.pop()
                    if x=="{":
                        flag-=1
                if i=="]":
                    x=stack.pop()
                    if x=="[":
                        flag-=1
            else:
                return False
        if flag==0 and len(stack)==0:
            return True
        else:
            return False
        
        