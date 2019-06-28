"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def traverse(self, tree1, tree2):
        if (not tree1 and not tree2):
            return True
        if(tree1 and tree2) and (tree1.val == tree2.val):
            return self.traverse(tree1.left, tree2.left) and self.traverse(tree1.right, tree2.right)
        
        else:
            return False
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        return self.traverse(p,q)
        