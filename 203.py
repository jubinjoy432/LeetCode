#remove linkedlist elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=head
        while temp:
            if temp==head and temp.val==val:
                head=head.next
                temp=head
            elif temp.next and temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head