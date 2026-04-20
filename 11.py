#Container With Most Water
class Solution(object):
    def maxArea(self, height):
        maxar=0
        i=0
        j=len(height)-1
        while i<j:
            maxar=max(min(height[i],height[j])*(j-i),maxar)
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1           
        return maxar
        