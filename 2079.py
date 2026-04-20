#Watering Plants
class Solution(object):
    def wateringPlants(self, plants, capacity):
        steps=0
        c=capacity
        for i in range(len(plants)):
            if plants[i]<=c:
                c=c-plants[i]
                steps=steps+1
            else:
                steps=steps+2*i+1
                c=capacity-plants[i]
        return steps
        