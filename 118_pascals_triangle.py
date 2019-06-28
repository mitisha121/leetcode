"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []
        
        triangle = []
        
        for i in range(0, numRows):
            row = []
            if i == 0:
                row.append(1)
                
            elif i == 1:
                row.append(1)
                row.append(1)
                   
            else:
                for j in range(i+1):
                    print(j)
                    if j == 0:
                        row.append(1)
                    elif j == i:
                        row.append(1)
                    else:
                        num = triangle[i-1][j] + triangle[i-1][j-1]
                        row.append(num)

            triangle.append(row)
            
        return triangle