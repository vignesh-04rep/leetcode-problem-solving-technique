#i almost done but could not able to do the all test cases
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # initialization
        cum_sum = sum(nums[0:k])
        maximum = cum_sum

        for i in range(k,len(nums)):
            cum_sum = cum_sum + nums[i] - nums[i-k]
            if cum_sum > maximum:
                maximum = cum_sum

        return float(maximum)/k
        