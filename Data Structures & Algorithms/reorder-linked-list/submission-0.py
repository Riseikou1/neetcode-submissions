# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slower,faster = head,head.next
        while faster and faster.next :
            faster = faster.next.next
            slower = slower.next
        
        right = slower.next
        prev = slower.next = None
        while right :
            tmp = right.next
            right.next = prev
            prev = right
            right = tmp
        
        while prev :
            tmp1,tmp2 = head.next,prev.next
            head.next = prev
            prev.next = tmp1
            head,prev = tmp1,tmp2
