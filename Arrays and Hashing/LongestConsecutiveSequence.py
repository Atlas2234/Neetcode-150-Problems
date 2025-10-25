"""
Time Complexity is O(n)
Space Complexity is O(n)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set from the list to allow O(1) lookups
        numSet = set(nums)
        longest = 0
        # Iterate through each number in the set
        for num in numSet:
            # Check if it's the start of a sequence
            if (num - 1) not in numSet:
                length = 1
                # Count the length of the sequence
                while (num + length) in numSet:
                    length += 1
                # Update the longest length found 
                longest = max(length, longest)
        return longest