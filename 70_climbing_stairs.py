"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        ways = [1,1]
        for i in range(2, n+1):
            ways.append(ways[i-1] + ways[i-2])
        
        return ways[n]


"""
Runtime: 16 ms, faster than 83.96% of Python online submissions for Climbing Stairs.
Memory Usage: 11.8 MB, less than 40.11% of Python online submissions for Climbing Stairs.
"""