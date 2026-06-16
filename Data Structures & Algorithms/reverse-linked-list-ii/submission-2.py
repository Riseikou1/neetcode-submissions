# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy

        for _ in range(left - 1) :
            cur = cur.next

        left_prev = cur
        left_head = cur.next
        cur.next = prev = None

        cur = left_head
        for _ in range(left, right + 1) :
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        left_head.next = cur
        left_prev.next = prev

        return dummy.next
