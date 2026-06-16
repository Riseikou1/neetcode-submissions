# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(a, b) :
            while b :
                a, b = b, a % b
            return a

        cur = head
        while cur.next :
            a = cur
            b = cur.next
            c = ListNode(helper(a.val, b.val), b)
            a.next = c 
            cur = b

        return head
