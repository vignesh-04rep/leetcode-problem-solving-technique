#just easy
def largestAltitude(self, gain):
        avg=maxi=0
        for i in gain:
            avg+=i
            maxi=max(maxi,avg)
        return maxi