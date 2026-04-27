#PAlindrome linked list
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=[]
        temp=head
        while temp:
            s.append(temp.val)
            temp=temp.next
        return s==s[::-1]