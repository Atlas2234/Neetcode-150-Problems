"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
from ast import List

class Solution:
    # Two pointer approach
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers and result variable
        l, r = 0, len(heights) - 1
        # Initialize result variable
        res = 0
        # Use two-pointer technique to find the maximum area
        while l < r:
            # Calculate the area
            area = min(heights[l], heights[r]) * (r - l)
            # Update the result if the current area is larger
            res = max(res, area)
            # Move the pointer pointing to the shorter line inward
            if heights[l] <= heights[r]:
                # Move left pointer to the right
                l += 1
            # Move right pointer to the left
            else:
                r -= 1
        # Return the maximum area found
        return res