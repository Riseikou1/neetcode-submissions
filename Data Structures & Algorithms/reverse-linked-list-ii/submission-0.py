# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = dummy = ListNode(0, head)
        for _ in range(left - 1) :
            cur = cur.next

        left_bound = cur
        reverse_head = cur.next

        for _ in range(right - left + 1) :
            cur = cur.next

        left_over = cur.next if cur else None

        prev = None
        cur = left_bound.next

        for _ in range(right - left + 1) :
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        left_bound.next = prev
        reverse_head.next = left_over

        return dummy.next