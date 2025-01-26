#i almost there 
class Solution:
    def uniqueOccurrences( self,arr):
        arr.sort()
        v = []

        i = 0
        while i < len(arr):
            cnt = 1

            # Count occurrences of the current element
            while i + 1 < len(arr) and arr[i] == arr[i + 1]:
                cnt += 1
                i += 1

            v.append(cnt)
            i += 1

        v.sort()

        for i in range(1, len(v)):
            if v[i] == v[i - 1]:
                return False

        return True
#the best solution
 def uniqueOccurrences(self, arr):
        d1 = {}
        for i in arr:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        l1 = list(d1.values())
        s1 = set(d1.values())
        return len(l1)== len(s1)