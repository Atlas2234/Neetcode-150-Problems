"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
from rpds import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize result list
        res = []
        # Sort the input list
        nums.sort()

        # Iterate through the list
        for i, a in enumerate(nums):
            # Break early if the current number is greater than 0
            if a > 0:
                break

            # Skip duplicate values to avoid repeating triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Initialize two pointers
            l, r = i + 1, len(nums) - 1
            # Use two-pointer technique to find pairs that sum to the negative of the current number
            while l < r:
                # Calculate the sum of the triplet
                threeSum = a + nums[l] + nums[r]
                # Move the pointers based on the comparison of threeSum and 0
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res