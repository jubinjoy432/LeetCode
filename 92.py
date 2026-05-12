#Reverse Linked List II
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count=0
        temp=head
        bef=head
        mid=None
        aft=None
        if left==right:
            return head
        if left==1:
            mid=head
        else:
            while temp:
                count+=1
                if count+1==left:
                    mid=temp.next
                    temp.next=None
                    break
                temp=temp.next
        temp=mid
        while temp:
            count+=1
            if count==right:
                aft=temp.next
                temp.next=None
                break
            temp=temp.next
        temp=mid
        d=ListNode(0)
        l=d
        while temp:
            y=temp.next
            x=l.next
            l.next=temp
            temp.next=x
            temp=y
        if left!=1:
            temp=bef
            while temp.next:
                temp=temp.next
            temp.next=d.next
        temp=d
        while temp.next:
            temp=temp.next
        temp.next=aft
        if left==1:
            return d.next
        else:
            return bef