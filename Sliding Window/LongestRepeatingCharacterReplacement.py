"""
Time Complexity: O(26 * N) = O(N), where N is the length of the input string s.
Space Complexity: O(1), since the size of the character set is fixed (26 uppercase English letters).
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize the result variable to store the maximum length found
        res = 0
        # Create a set of unique characters in the string
        charSet = set(s)

        # Iterate through each unique character in the set
        for c in charSet:
            count = l = 0
            # Use a sliding window approach to find the longest substring
            for r in range(len(s)):
                # Increment count if the current character matches the target character
                if s[r] == c:
                    count += 1
                # If the number of characters to replace exceeds k, shrink the window from the left
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                # Update the result with the maximum length found
                res = max(res, r - l + 1)
        return res