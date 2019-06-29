"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
"""

class Solution(object):
    def pascalTriangle(self, numRows):
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
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = self.pascalTriangle(rowIndex+1)
        
        return triangle[rowIndex]
        

"""
Your memory usage beats 71.54 % of python submissions.
Your runtime beats 89.43 % of python submissions.
"""