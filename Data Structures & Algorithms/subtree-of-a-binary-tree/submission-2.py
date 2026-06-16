# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(head1, head2) :
            if not head1 or not head2 :
                return not head1 and not head2

            if head1.val != head2.val :
                return False
            
            return helper(head1.left, head2.left) and helper(head1.right, head2.right)

        if not root : return False

        if helper(root, subRoot) :
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

