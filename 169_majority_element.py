"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        max_count_num = float('-inf')
        
        for num in nums:
            if num not in count_dict.keys():
                count_dict[num] = nums.count(num)
                if num > max_count_num and nums.count(num) > int(len(nums)/2):
                    max_count_num = num
                    
        return max_count_num


"""
Your runtime beats 57.09 % of python submissions.
Your memory usage beats 73.46 % of python submissions.
"""