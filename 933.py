class RecentCounter(object):

    def __init__(self):
        self.count=0
        self.queue=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        x=t-3000
        while(self.queue[0]<x):
            self.queue.pop(0)
        return len(self.queue)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)