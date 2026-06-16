# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists : return None
        def helper(l1, l2) :
            dummy = cur = ListNode()
            while l1 and l2 :
                if l1.val <= l2.val :
                    cur.next = l1
                    l1 = l1.next
                else :
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            cur.next = l1 or l2
            return dummy.next

        while len(lists) > 1 :
            new_list = []
            for i in range(0, len(lists), 2) :
                first = lists[i]
                second = lists[i + 1] if (i + 1) < len(lists) else None
                new_list.append(helper(first, second))
            lists = new_list

        return lists[0]
