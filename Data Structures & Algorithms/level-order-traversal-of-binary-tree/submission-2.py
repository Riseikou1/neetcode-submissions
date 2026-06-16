# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []
        res = []
        q = deque([root])
        while q :
            new_list = list()
            for _ in range(len(q)) :
                cur = q.popleft()
                new_list.append(cur.val)
                if cur.left :
                    q.append(cur.left)
                if cur.right :
                    q.append(cur.right)

            res.append(new_list)
        return res
