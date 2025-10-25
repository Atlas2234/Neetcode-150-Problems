"""
Naive solution for finding the k most frequent elements in a list.

Time complexity is O(n log n) due to the sorting step.
Space complexity is O(n) for storing the frequency counts.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count the frequency of each element in the list
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Create a list of [frequency, element] pairs
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        # Sort the list based on frequency
        arr.sort()

        # Extract the k most frequent elements
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
"""

"""
A faster solution using modified bucket sort.

Time complexity is O(n) on average.
Space complexity is O(n) for the dictionary and buckets.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # Create n + 1 empty buckets where n is the length of the input list

        # Count the frequency of each element in the list
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Place each number in the corresponding frequency bucket
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1): # Iterate through the frequency buckets in reverse order.
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res