#Really amazing problem sofar but i failed to solved it i don't know how to solve the multiplication 
# of previous and next values so seen the solution 
class Solution:
    def productExceptSelf(self, nums):
        pre=1
        suf=1
        cv=0
        out=[]
        for i in range(len(nums)):
            cv= nums[suf] * nums[i]
            out.append(cv)
        while pre == 0:
            cv=nums[pre]*nums[j]
            out.append(cv)
            pre-=1
        return out
#the actuall solution was

 output = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
    
        return output        
     