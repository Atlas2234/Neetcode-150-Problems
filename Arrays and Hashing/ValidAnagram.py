"""
Time complexity is O(n + m) where n and m are the legnths of strings s and t. This is because we iterate through
both strings once to build the character count dictionaries and then compare the two dictionaries which takes O(min(n, m)) time.

Space complexity is O(1) because the size of the character count dictionaries is bounded by the number of unique characters, which is constant (e.g., 26 for lowercase English letters).

class Solution:
    # Construct the character count dictionary for a given string
    def countString(self, s: str) -> dict:
        chDict = {}
        for ch in s:
            if ch not in chDict:
                chDict[ch] = 1
            else:
                chDict[ch] += 1
        return chDict

    def isAnagram(self, s: str, t: str) -> bool:
        # Check if s and t are empty or a single char
        if s == '' and t == '':
            return True
        
        if len(s) == 1 and len(t) == 1 and s == t:
            return True
        
        # Construct the dictionary to count letters in string s
        sDict = self.countString(s)
        tDict = self.countString(t)

        # Compare the two dictionaries
        if sDict == tDict:
            return True
        
        return False
"""

"""
Cleaner solution with time complexity of O(n) since it loops through the string only once, using a single dictionary
to count characters.

Space complexity is O(1) because the size of the character count dictionary is bounded by the number of unique characters, which is constant (e.g., 26 for lowercase English letters).
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize the dictionary
        checkDict = {}

        # Initialize an empty list to store the result
        l = []

        # Iterate through each element in the list
        for i in range(len(nums)):
            # Calculate the other number needed to reach the target
            pkey = target - nums[i]
            # Check if the other number is already in the dictionary
            if pkey not in checkDict:
                # Add the current number and its index to the dictionary
                checkDict[nums[i]] = i
            elif pkey in checkDict and checkDict[pkey] != i:
                # If found, set the result list with the indices of the other number and the current number
                l = [checkDict[pkey], i]
            
        # Return the list of indices
        return l