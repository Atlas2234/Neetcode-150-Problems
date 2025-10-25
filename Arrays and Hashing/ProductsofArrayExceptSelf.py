"""
Time Complexity: O(N), where N is the length of the input list nums.
We traverse the list a constant number of times (three passes), resulting in linear time complexity.

Space Complexity: O(1) if we do not count the output list, as we use a fixed amount of extra space. 
But if we consider the output list, it is O(N) since we store N elements in the output.
"""

from rpds import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeroProd = 1
        nonZeroProd = 1

        outputList = []

        zerocount = 0

        # multiply all numbers
        for n in nums:
            if n == 0:
                zerocount += 1
            zeroProd *= n
        
        # multiply all numbers, excluding 0
        for n in nums:
            if n != 0:
                nonZeroProd *= n

        # create output list
        for n in range(len(nums)):
            # handle cases based on number of zeros
            # if one zero, only the index with zero gets the product of non-zero numbers
            if nums[n] == 0 and zerocount == 1:
                outputList.append(nonZeroProd)
            # if more than one zero, all indices get 0
            elif nums[n] == 0 and zerocount > 1:
                 outputList.append(zeroProd)
            # if no zeros, each index gets total product divided by the number at that index so as to exclude it
            else:
                outputList.append(int(zeroProd / nums[n]))
        
        return outputList

"""
A method to solve the problem without using division.
Time Complexity: O(N), where N is the length of the input list nums.
We traverse the list a constant number of times (three passes), resulting in linear time complexity.

Space Complexity: O(1) if we do not count the output list, as we use a fixed amount of extra space. But if we consider the output list, it is O(N) since we store N elements in the output.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize prefix and suffix product arrays
        prefixArray = []

        suffixArray = []

        outputArray = []
        
        # Calculate prefix products
        prefixProduct = 1
        for i in range(len(nums)):
            if i - 1 >= 0:
                prefixProduct *= nums[i - 1]
            # Append the current prefix product
            prefixArray.append(prefixProduct)

        # Calculate suffix products
        suffixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            if i + 1 < len(nums):
                suffixProduct *= nums[i + 1]
            # Insert at the beginning to maintain order
            suffixArray.insert(0, suffixProduct)
        
        # Calculate the result by multiplying prefix and suffix products
        for i in range (len(nums)):
            outputArray.append(prefixArray[i] * suffixArray[i])
        
        return outputArray