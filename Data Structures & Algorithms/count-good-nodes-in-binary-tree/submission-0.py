# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node,parent_val):
            if not node :
                return 0

            if node.val >= parent_val :
                self.count += 1
                parent_val = node.val

            dfs(node.left,parent_val)
            dfs(node.right,parent_val)


        dfs(root,float('-inf'))
        return self.count