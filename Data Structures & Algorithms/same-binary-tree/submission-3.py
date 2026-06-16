# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stkP = [p]
        stkQ = [q]

        while stkP and stkQ :
            nodeP = stkP.pop()
            nodeQ = stkQ.pop()
            if not nodeP and not nodeQ : continue
            if not nodeP or not nodeQ or nodeP.val != nodeQ.val :
                return False

            stkP.append(nodeP.left)
            stkP.append(nodeP.right)
            stkQ.append(nodeQ.left)
            stkQ.append(nodeQ.right)

        return True
            
