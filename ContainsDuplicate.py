"""
Time compleixty average case us O(n) because you iterate the list once, doing constant-time hash map lookups and inserts per element on average.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a dictionary to keep track of unique numbers. Used to keep track of which numbers have been seen.
        uniqueDict = {}

        # Iterate through each number in the list
        for num in nums:
            # If the number is not in the dictionary, add it. Otherwise, return true.
            if uniqueDict.get(num) == None:
                uniqueDict[num] = 1
            elif uniqueDict.get(num) != None:
                return True
        return False
"""

"""
Cleaner solution that uses a hash set instead of a dictionary.
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False