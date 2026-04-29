#circular sentence
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        flag=True
        l=len(sentence)
        for i in range(l):
            if sentence[i]==" " and sentence[i-1]!=sentence[i+1]:
                flag=False
        if sentence[0]!=sentence[l-1]:
            flag=False
        return flag