"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from ast import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0

        while i <= len(numbers) - 2:
            j = i + 1
            while j <= len(numbers) - 1:
                print(j)
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                j += 1

            i += 1

        
        return []


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        l, r = 0, len(numbers) - 1

        # Use the two-pointer technique to find the two numbers that add up to the target
        while l < r:
            # Calculate the current sum of the two pointed numbers
            curSum = numbers[l] + numbers[r]

            # Move the pointers based on the comparison of curSum and target. Can do this because the array is sorted.
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []