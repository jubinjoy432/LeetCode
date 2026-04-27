#convert binary in linked list to decimal
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp=head
        s=[]
        dec=0
        while temp:
            s.append(temp.val)
            temp=temp.next
        n=len(s)-1
        for i in s:
            dec=dec+2**n*i
            n-=1
        return dec
    
########################OR###############################333
def getDecimalValue(self, head: Optional[ListNode]) -> int:
    num=0
    while head:
        num(n<<1)|head.val
        head=head.next
    return num
