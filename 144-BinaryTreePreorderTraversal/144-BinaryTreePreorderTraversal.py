# Last updated: 8/12/2026, 11:51:17 AM
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        stack = [root]

        while stack:
            current_node = stack.pop()
            result.append(current_node.val)

            # Push right child first, then left child
            # so that left child is processed before right child (LIFO stack)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        
        return result