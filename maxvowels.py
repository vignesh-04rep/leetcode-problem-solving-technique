#this the solution actually i came up with    

def maxVowels(self,s, k):
        d=out=0
        while d < len(s):
            for i in range(k):
                if i == "a" or "e" or "i" or "o" or "u":
                    out=+1
        d+=1
        return out
