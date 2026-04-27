#Simplify Path
class Solution(object):
    def simplifyPath(self, path):
        stack=[]
        pa=path.split("/")
        for p in pa:
            if p=="" or p==".":
                continue
            elif p=="..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(p)
        return "/"+"/".join(stack)
            