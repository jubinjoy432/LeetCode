#merge nodes in bw zeroes
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        sum=0
        dummy=ListNode(0)
        d=dummy
        while temp:
            if temp.val==0:
                if sum!=0:
                    x=ListNode(sum)
                    d.next=x
                    d=d.next
                    sum=0
            else:
                sum+=temp.val
            temp=temp.next

        return dummy.next