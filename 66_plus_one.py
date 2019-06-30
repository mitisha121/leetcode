"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        number = 0
        j = n-1
        for i in range(n):
            number += (digits[i])*(10**j)
            j -=1
            
        number += 1
        
        return list(str(number))
        
        
"""
Runtime: 12 ms, faster than 98.54% of Python online submissions for Plus One.
Memory Usage: 11.7 MB, less than 79.95% of Python online submissions for Plus One.
"""