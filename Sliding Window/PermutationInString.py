"""
Time Complexity: O(n*m) where n is len(s2) and m is len(s1)
Space Complexity: O(1) since the size of the character set is fixed (26 lowercase English letters).
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) == 1 and len(s1) == 1:
            if s1 == s2:
                return True
            else:
                return False

        s1dict = {} # space O(1)
        
        # Create s1dict to check if characters are in s1
        # O(m) where m is size of s1
        for c in s1:
            if c in s1dict:
                s1dict[c] += 1
            else:
                s1dict.update({c:1})
        
        # Create fixed sliding window
        i = 0
        j = len(s1) - 1

        # Loop through s2 with sliding window and check if each character in the window matches the s1set
        # Main loop O(n) where n is len(s2)
        while j < len(s2):
            tempDict = {} # space O(1)
            # Loop through each window.
            # O(m)
            k = i
            while k <= j:
                if s2[k] in tempDict:
                    tempDict[s2[k]] += 1
                else:
                    tempDict.update({s2[k]:1})
                k += 1
            print(tempDict)
            if tempDict == s1dict:
                return True
                
            i += 1
            j += 1

        return False
    
"""
Time Complexity: O(n), where n is the length of s2.
Space Complexity: O(1), since the size of the character set is fixed (26 lowercase English letters).
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Early return if s1 is longer than s2
        if len(s1) > len(s2):
            return False
        # Initialize frequency counts for both strings
        s1Count, s2Count = [0] * 26, [0] * 26
        # Populate the frequency counts for the first window
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        # Initialize matches to count how many characters have matching frequencies
        matches = 0
        # Count initial matches
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        # Slide the window over s2
        l = 0
        for r in range(len(s1), len(s2)):
            # If all characters match, return True
            if matches == 26:
                return True
            # Add the new character to the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # Update matches for the added character
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            # Remove the character going out of the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # Update matches for the removed character
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        # Final check for the last window
        return matches == 26