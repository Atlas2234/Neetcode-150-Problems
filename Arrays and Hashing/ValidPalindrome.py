"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        findex = 0
        bindex = len(s)- 1

        while findex <= bindex:
            if not s[findex].isalnum():
                findex += 1
                continue
            
            if not s[bindex].isalnum():
                bindex -= 1
                continue

            if s[findex] != s[bindex]:
                return False

            findex += 1
            bindex -= 1
        
        return True