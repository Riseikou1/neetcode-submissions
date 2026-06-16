# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root : return True
        
        def helper(node) :
            if not node : return (0, True)

            left, left_bal = helper(node.left)
            right, right_bal = helper(node.right)

            balance = abs(left - right) <= 1
            is_balanced = left_bal and right_bal and balance

            return (1 + max(left, right), is_balanced)

        return helper(root)[1]
