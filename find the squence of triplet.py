# i think i did not completly understand the question but i came up with the solution bt it does 
# not applicable for all test case

class Solution(object):
    def increasingTriplet(self, nums):
       res=[]
       p=1
       for i in nums[:-1]:
        if i < nums[p] and i>0:
            p+=1
        elif  nums[-1] > nums[-2] and nums[-2] > nums[-3]:
            return True
        else:
            return False
       return True
    

#the original solution



class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n  # smallest so far
            elif n <= second:
                second = n  # second smallest
            else:
                return True  # found a triplet
        
        return False