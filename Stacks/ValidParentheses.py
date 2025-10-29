"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize a stack to keep track of opening brackets
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        # Iterate through each character in the string
        for c in s:
            # If the character is a closing bracket, check for a matching opening bracket
            if c in closeToOpen:
                # If the stack is not empty and the top of the stack matches the corresponding opening bracket, pop it
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # If there is no match, return False
                else:
                    return False
            # If the character is an opening bracket, push it onto the stack
            else:
                stack.append(c)

        return True if not stack else False