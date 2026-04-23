#Time Needed to Buy Tickets
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        queue=deque()#type:ignore
        for i in range(len(tickets)):
            queue.append(i)
        d={}
        count=0
        for i in range(len(tickets)):
            d[i]=tickets[i]
        while queue:
            if d[k]==0:
                return count
            elif d[queue[0]]==0:
                queue.popleft()
            else:
                count+=1
                d[queue[0]]-=1
                queue.append(queue.popleft())