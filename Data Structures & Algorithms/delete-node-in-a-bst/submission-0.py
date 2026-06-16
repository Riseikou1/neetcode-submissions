# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root : return None

        def helper(node) :
            while node.left :
                node = node.left
            return node.val

        if root.val > key :
            root.left = self.deleteNode(root.left, key)
        elif root.val < key :
            root.right = self.deleteNode(root.right, key)
        else :  # the node to be deleted was found.
            if not root.left and not root.right :return None
            if not root.right :return root.left
            if not root.left : return root.right

            # it has 2 children.
            #find the predecessor. and change with root.val and delete that predecessor.
            successor_val = helper(root.right)
            root.val = successor_val
            root.right = self.deleteNode(root.right, successor_val)

        return root

