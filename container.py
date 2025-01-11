def maxArea(self, height):
        la=sl=d=0
        while d <len(height)-1:
            if height[la] <= height[sl+1]:
                la = sl+1
            sl+=1
            d+=1
        return height[sl]*height[sl]
#the solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        