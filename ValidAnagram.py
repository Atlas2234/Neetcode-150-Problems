"""
Time complexity is O(n + m) where n and m are the legnths of strings s and t. This is because we iterate through
both strings once to build the character count dictionaries and then compare the two dictionaries which takes O(min(n, m)) time.

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
Cleaner solution with same time complexity.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if lengths differ
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # Count characters in both strings
        for i in range(len(s)):
            # Update counts for s and t. Uses get method to handle missing keys.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare the two count dictionaries
        return countS == countT