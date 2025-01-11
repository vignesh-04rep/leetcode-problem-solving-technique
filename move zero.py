#i done this problem with my own code but i did not statisfies all edgecase
 def moveZeroes(self, nums):
        null=0
        for j in range(len(nums)-1,-1,-1):
            break
        for i in range(len(nums)): 
            if nums[i] == null:
                nums[i],nums[j] = nums[j],nums[i]
                j-=1
            if j == i:
                break
        return nums
#the solution i submit
class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums
