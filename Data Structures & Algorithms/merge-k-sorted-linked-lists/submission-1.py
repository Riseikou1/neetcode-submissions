# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper :
    def __init__(self,node):
        self.node = node
    
    def __lt__(self,other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return None
        
        dummy = cur = ListNode()
        minHeap = list()

        for lst in lists :
            if lst :
                heapq.heappush(minHeap,NodeWrapper(lst))

        while minHeap :
            wrapped_node = heapq.heappop(minHeap)
            cur.next = wrapped_node.node
            cur = cur.next

            if wrapped_node.node.next :
                heapq.heappush(minHeap,NodeWrapper(wrapped_node.node.next))

        return dummy.next
