# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slower,faster = head,head
        while faster and faster.next :
            faster = faster.next.next
            slower = slower.next
            if faster == slower :
                return True
        return False

