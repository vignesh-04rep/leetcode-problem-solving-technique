#best solution for sliding window mine was so different for required specification

def findMaxAverage(self, nums, k):
        window = sum(nums[:k])
        max_sum = window
        
        for i in range(len(nums) - k):
            window = window - nums[i] + nums[i + k]
            max_sum = max(max_sum, window)
        
        return max_sum / k
    
