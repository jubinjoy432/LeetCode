class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        i=0
        j=len(plants)-1
        ca,cb=capacityA,capacityB
        refill=0
        while i<=j:
            if plants[i]<=ca:
                ca=ca-plants[i]
            else:
                refill+=1
                ca=capacityA-plants[i]
            i+=1
            if plants[j]<=cb:
                cb=cb-plants[j]
            else:
                refill+=1
                cb=capacityB-plants[j]
            j-=1
            if i==j:
                if ca>cb or ca==cb:
                    if plants[i]<=ca:
                        ca=ca-plants[i]
                    else:
                        refill+=1
                        ca=capacityA-plants[i]
                    i+=1
                else:
                    if plants[j]<=cb:
                        cb=cb-plants[j]
                    else:
                        refill+=1
                        cb=capacityB-plants[j]
                    j-=1

        return refill
        