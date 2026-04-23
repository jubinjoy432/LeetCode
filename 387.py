#First Unique Character in a String
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue=[]
        x=[]
        for i in s:
            if queue:
                if i in queue:
                    x.append(i)
                    queue.remove(i)
                elif i not in x:
                    queue.append(i)
            elif i not in x:
                queue.append(i)
        if queue:
            return s.index(queue.pop(0))
        else:
            return -1