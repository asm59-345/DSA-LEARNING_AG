class Solution:
    def maxArea(self, height: List[int]) -> int:
        left =0
        right = len(height) -1
        max_water = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])

            max_water = max(max_water, current_height * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water