#Add two numbers
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=b=c=0
        while l1:
            a=a*10+l1.val
            l1=l1.next
        while l2:
            b=b*10+l2.val
            l2=l2.next
        c=a+b
        d=ListNode(0)
        l=d
        while c!=0:
            x=ListNode(c%10)
            x.next=l.next
            l.next=x
            c=c//10
        if not d.next:
            x=ListNode(0)
            d.next=x
        return d.next