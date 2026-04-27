#Remove Duplicates from Sorted List II
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        h=ListNode()
        h.next=head
        prev=h
        while prev.next and prev.next.next:
            if prev.next.val==prev.next.next.val:
                temp=prev.next
                while temp and temp.val==prev.next.val:
                    temp=temp.next
                prev.next=temp
            else:
                prev=prev.next
        return h.next