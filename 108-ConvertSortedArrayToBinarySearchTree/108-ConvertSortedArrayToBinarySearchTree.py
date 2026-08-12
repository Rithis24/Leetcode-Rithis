# Last updated: 8/12/2026, 11:51:31 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build_bst_recursive(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            root = TreeNode(nums[mid])
            
            root.left = build_bst_recursive(left, mid - 1)
            root.right = build_bst_recursive(mid + 1, right)
            
            return root
            
        return build_bst_recursive(0, len(nums) - 1)