# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root : return False
        if not subRoot : return True

        def helper(a, b) :
            stack = [(a, b)]
            while stack :
                node1, node2 = stack.pop()
                if not node1 and not node2 : continue
                if not node1 or not node2 or node1.val != node2.val :
                    return False

                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))

            return True

        q = deque([root])
        while q :
            node = q.popleft()
            if node.val == subRoot.val and helper(node, subRoot) :
                return True
            if node.left :
                q.append(node.left)
            if node.right :
                q.append(node.right)

        return False

