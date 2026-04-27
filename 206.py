#Reverse linked list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        d=ListNode(0)
        l=d
        while temp:
            y=temp.next
            x=l.next
            l.next=temp
            temp.next=x
            temp=y
        return d.next