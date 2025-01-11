def isSubsequence(self,s, t):
        if s == "":
            return True
        count=0
        for a in range(len(s)):
            break
        if a<
        for b in t:
            if s[a] == b:
                a+=1
                count+=1
        return count ==len(s)
#the error bargin become smaller and smaller
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)