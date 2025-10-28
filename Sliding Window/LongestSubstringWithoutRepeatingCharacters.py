"""
Time complexity is O(n) because we traverse the string once.
Space complexity is O(min(m, n)), where m is the size of the character set and n is the length of the string. This is because the sliding window can contain at most min(m, n) characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize two pointers and a set to keep track of characters in the current substring
        i, j = 0, 1
        # Set to keep track of unique characters in the current substring
        if len(s) > 0:
            checkSet = {s[i]}
        # Edge case: if the string length is 1, return 1
        if len(s) == 1:
            return 1
            
        currentMax = 0
        tempMax = 0

        # Iterate through the string with the second pointer
        while j < len(s):
            # If the character at the second pointer is not in the set,
            if s[j] not in checkSet:
                checkSet.add(s[j])
                # Update tempMax to the length of the current substring
                tempMax = j + 1 - i
                # Move the second pointer forward
                j += 1
            # If the character at the second pointer is already in the set,
            elif s[j] in checkSet:
                # Update currentMax if tempMax is greater
                if tempMax > currentMax:
                    currentMax = tempMax
                # Move the first pointer to remove characters until the duplicate is removed
                while i < j:
                    # Remove characters from the set until the duplicate character is removed
                    if s[i] != s[j]:
                        checkSet.remove(s[i])
                        i += 1
                    # If the characters are equal, move the first pointer and update tempMax
                    elif s[i] == s[j]:
                        i += 1
                        # Update tempMax to the length of the current substring
                        tempMax = j + 1 - i
                        break
                # Move the second pointer forward
                j += 1
        # After the loop, return the maximum of tempMax and currentMax
        return max(tempMax, currentMax)
