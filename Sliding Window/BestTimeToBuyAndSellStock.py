"""
Time complexity is O(n) because we traverse the prices list once.
Space complexity is O(1) since we are using only a fixed amount of extra space.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize two pointers and a variable to track the current maximum profit
        i, j = 0, 1
        # Variable to keep track of the maximum profit found so far
        currentprofit = 0

        # Iterate through the prices list with the second pointer
        while j < len(prices):
            # If the price at the first pointer is greater than the price at the second pointer,
            if prices[i] > prices[j]:
                i = j
                j = j + 1
            # If the price at the first pointer is less than or equal to the price at the second pointer,
            elif prices[i] <= prices[j] and prices[j] - prices[i] > currentprofit:
                currentprofit = prices[j] - prices[i]
                j = j + 1
            # If the price difference does not yield a higher profit,
            else:
                j = j + 1
        # Return the maximum profit found
        return currentprofit