#so what is the majaor takeway from this problem is simply to sort an array and use 
# two pointer apporach
def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]
        