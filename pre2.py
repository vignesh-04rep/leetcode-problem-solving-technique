# i cloud not reach the answeer
def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = sum(nums)
        left = 0
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        
        return -1
            