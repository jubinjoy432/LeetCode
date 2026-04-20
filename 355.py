# Reverse Vowels of a String
class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        left=0
        right=len(s)-1
        while left<right:
            while s[left] not in "aeiouAEIOU" and left<right:
                left=left+1
            while s[right] not in "aeiouAEIOU" and right>left:
                right=right-1
            s[left],s[right]=s[right],s[left]
            left=left+1
            right=right-1
        s="".join(s)
        return s