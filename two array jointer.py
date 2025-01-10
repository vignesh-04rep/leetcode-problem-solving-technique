#at first we need to create an array variable "res" to store an values then we iterate through it 
#and with the another variable but not in res 
#piece of cake
class Solution(object):
    def intersection(self, nums1, nums2):
        maxi=max(len(nums1),len(nums2))
        a=[]
        for i in nums1:
            if i in nums2 and i not in a:
                a.append(i)
        return a
        
        