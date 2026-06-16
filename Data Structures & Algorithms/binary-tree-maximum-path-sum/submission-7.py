# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(node) :
            if not node : return 0

            leftie = max(0, dfs(node.left))
            rightie = max(0, dfs(node.right))

            self.res = max(self.res, node.val + leftie + rightie)
            return node.val + max(leftie, rightie)

        dfs(root)
        return self.res
