#min stack
class MinStack:

    def __init__(self):
        self.s=[]
        self.mini=[]

    def push(self, val: int) -> None:
        if not self.s:
            self.mini.append(val)
        elif val<=self.mini[-1]:
            self.mini.append(val)
        self.s.append(val)

    def pop(self) -> None:
        if self.s[-1]==self.mini[-1]:
            self.mini.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()