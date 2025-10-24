"""
Time complexity average case is O(n^2) because you iterate the list twice in a nested loop.
Space complexity is O(1) because we are not using any additional data structures that grow with input size.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty list to store the result
        l = []
        # Iterate through each element in the list
        for i in range(len(nums)):
            for j in range(len(nums)):
                # Check if the indices are different and if the sum equals the target
                if j > i and (nums[i] + nums[j]) == target:
                    l.append(i)
                    l.append(j)
        return l
"""

"""
Cleaner solution that uses a hash set instead of a dictionary.
Time complexity is O(n) because you iterate through the list once, doing constant-time hash map lookups and inserts per element on average.
Space complexity is O(n) in the worst case, where all elements are unique and stored in the hash map.
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False