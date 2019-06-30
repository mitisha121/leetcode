"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    
    def inorder(self, root):
        result = []
        if not root:
            return [None]
        
        result = [root.val]
        result += self.inorder(root.left) 
        result += self.inorder(root.right)
        return result
    
    def inorder2(self, root):
         
        if root is None:
            return [None]
        
        result = [root.val]
        result += self.inorder2(root.right)
        result += self.inorder2(root.left) 
        return result

        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        if root is None:
            return True
        
        right_tree = self.inorder2(root.right)
        left_tree = self.inorder(root.left)
    
        return left_tree == right_tree
        
"""
Your runtime beats 96.66 % of python submissions.
Your memory usage beats 90.45 % of python submissions.
"""