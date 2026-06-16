# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_map = {val:idx for idx,val in enumerate(inorder)}
        self.pre_idx = 0
        def builder(l,r):
            if l > r :
                return None
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            split = self.inorder_map[root_val]
            root.left = builder(l,split-1)
            root.right = builder(split+1,r)

            return root

        return builder(0,len(inorder)-1)