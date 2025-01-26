
#i almost there to solve this problem but just miss
class Solution(object):
    def longestSubarray(self, nums):
        count=left=out=0
        for right in range(len(nums)):
            if nums[right]==0:
                count+=1
            while count > 1:
                if nums[left] == 0:
                    count-=1
                left+=1
            out=max(out,right-left)
        return out            