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
        
        sectionHead = cur
        cur = cur.next
        leftHead = cur
        prev = None
        for _ in range(right - left + 1) :
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        sectionHead.next = prev
        leftHead.next = cur

        return dummy.next
