# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy 
        carry = 0

        while l1 or l2 or carry :
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            total = val1 + val2 + carry
            carry, val = total // 10, total % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next

        return dummy.next
