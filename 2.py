#Add two numbers
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        dummy=ListNode(0)
        l=dummy
        while l1 and l2:
            s=l1.val+l2.val+c
            l.next=ListNode(s%10)
            c=s//10
            l1,l2=l1.next,l2.next
            l=l.next
        while l1:
            s=l1.val+c
            l.next=ListNode(s%10)
            c=s//10
            l1=l1.next
            l=l.next
        while l2:
            s=l2.val+c
            l.next=ListNode(s%10)
            c=s//10
            l2=l2.next
            l=l.next
        if c:
            l.next = ListNode(c)
        return dummy.next