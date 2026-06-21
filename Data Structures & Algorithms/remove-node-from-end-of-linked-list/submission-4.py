# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        faster, slower = dummy, dummy

        for _ in range(n + 1) :
            faster = faster.next

        while faster :
            faster = faster.next
            slower = slower.next

        slower.next = slower.next.next
        return dummy.next
