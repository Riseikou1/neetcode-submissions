# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getter(node, k) :
            while node and k > 0 :
                node = node.next
                k -= 1
            return node

        dummy = ListNode(0, head)
        groupPrev = dummy
        cur = head

        while True :
            kth = getter(groupPrev, k)
            if not kth : break
            groupNext = kth.next

            prev = kth.next
            while cur != groupNext :
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
    
        return dummy.next