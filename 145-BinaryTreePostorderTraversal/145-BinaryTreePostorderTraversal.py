# Last updated: 8/12/2026, 11:51:15 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack1 = [root]  # This stack is used to explore nodes in a modified pre-order fashion
        stack2 = []      # This stack will store nodes in the reverse of postorder (Root, Right, Left)

        while stack1:
            node = stack1.pop()
            stack2.append(node.val)

            # For the two-stack iterative postorder, stack1 is used to effectively do a
            # "root-right-left" traversal.
            # Because stack1 is LIFO, to process the right child first (then left),
            # we push the left child first, then the right child.
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        # Stack2 now contains elements in Root, Right, Left order.
        # Popping from stack2 will give us Left, Right, Root, which is postorder.
        while stack2:
            result.append(stack2.pop())
            
        return result