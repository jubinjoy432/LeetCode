#Remove Duplicates from Sorted List
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        h=head
        while h.next:
            if h.next.val==h.val:
                h.next=h.next.next
            else:
                h=h.next
        return head