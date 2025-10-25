"""
Time Complexity: O(N) for both encoding and decoding, where N is the total length of all strings.
Space Complexity: O(N) for the encoded string and the list of decoded strings.
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#': # Find the delimiter to extract the length of the next string
                j += 1 
            length = int(s[i:j]) # Convert the substring representing the length to an integer
            i = j + 1 # Move past the delimiter
            j = i + length # Calculate the end index of the string
            res.append(s[i:j]) # Extract the string and add it to the result list
            i = j

        return res
    
# For empty string

# So an empty string becomes "0#" in the encoded format.

# Decoding Empty Strings
# The decode process works perfectly for empty strings:

# Find the length: Reads 0 before the #
# Parse: length = 0
# Extract: s[i:j] where j = i + 0, so it extracts an empty string
# Append: Adds "" to the result list