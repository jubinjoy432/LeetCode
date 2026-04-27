#remove n th element from end of linked list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        count-=n
        if count==0:
            return head.next
        i=1
        temp=head
        while i<count and temp.next:
            temp=temp.next
            i+=1
        if temp.next.next:
            temp.next=temp.next.next
        else:
            temp.next=None
        return head