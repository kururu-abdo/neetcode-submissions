class Solution:
    def maxArea(self, heights: list[int]) -> int:
        # 1. Setup variables: Start as wide as possible
        max_area = 0
        left = 0
        right = len(heights) - 1
        
        # 2. Main loop: Keep going until pointers meet
        while left < right:
            # Calculate current width and height
            width = right - left
            current_height = min(heights[left], heights[right])
            
            # Update maximum area found so far
            current_area = width * current_height
            max_area = max(max_area, current_area)
            
            # 3. Dynamic adjustment: Move the shorter wall inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
