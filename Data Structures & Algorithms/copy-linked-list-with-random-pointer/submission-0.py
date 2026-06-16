"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return None
        book = {None:None}

        cur = head
        while cur:
            new = Node(cur.val)
            book[cur] = new
            cur = cur.next
        
        cur = head
        while cur:
            new = book[cur]
            new.next = book[cur.next]
            new.random = book[cur.random]
            cur = cur.next
        
        return book[head]

