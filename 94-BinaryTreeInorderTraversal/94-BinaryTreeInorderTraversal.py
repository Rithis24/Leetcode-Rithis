# Last updated: 8/12/2026, 11:51:37 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current is not None or stack:
            # Traverse to the leftmost node, pushing all visited nodes onto the stack
            while current is not None:
                stack.append(current)
                current = current.left
            
            # current is None, meaning we've reached the leftmost child of the top of the stack
            # Pop the node, add its value to result, and then move to its right child
            current = stack.pop()
            result.append(current.val)
            current = current.right
            
        return result