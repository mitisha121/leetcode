"""
Remove all elements from a linked list of integers that have value val.

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """       
        # Handles the case when there are duplicates of val 1  
        # in . linked list[1, 1, 1, 2]
        while(head and head.val == val):
            head = head.next
            
        result = head
        previous_node = head
        current_node = head
        
        # If linked list is [1] and val is 1, directly return
        if result and result.next is None and result.val == val:
            return
        
        # As long as the node exists and is not None,
        # if the current_node.val is val, remove the current_node
        # from the linked list by making the previous_node point to
        # the current_node.next
        while(current_node):
            if current_node.val == val:
                previous_node.next = current_node.next
            else:
                previous_node = current_node
            current_node = current_node.next
        
        return result