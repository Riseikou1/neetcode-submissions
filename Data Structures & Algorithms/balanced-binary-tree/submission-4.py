# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        mp = {None: (0, True)} # (height, balanced)
        stack = [root]

        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftBalanced = mp[node.left]
                rightHeight, rightBalanced = mp[node.right]

                height = 1 + max(leftHeight, rightHeight)
                balanced = (leftBalanced and rightBalanced
                            and abs(leftHeight - rightHeight) <= 1)

                mp[node] = (height, balanced)

        return mp[root][1]
