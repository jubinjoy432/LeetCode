#odd even linked list
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos=0
        temp=head
        o=ListNode(0)
        ol=o
        e=ListNode(0)
        el=e
        while temp:
            if pos==0:
                x=ListNode(temp.val)
                ol.next=x
                ol=ol.next
                pos=1
            else:
                x=ListNode(temp.val)
                el.next=x
                el=el.next
                pos=0
            temp=temp.next
        ol.next=e.next
        return o.next