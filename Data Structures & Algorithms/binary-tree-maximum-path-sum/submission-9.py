# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def helper(node) :
            if not node : return 0

            left  = max(0, helper(node.left)) 
            right = max(0, helper(node.right))
            self.res = max(self.res, left + right + node.val)

            return node.val + max(left, right)

        helper(root)
        return self.res
