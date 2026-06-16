class Node :
    def __init__(self, val, next = None, prev = None) :
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = Node(tokens[0])
        cur = head
        for i in range(1, len(tokens)) :
            cur.next = Node(tokens[i], prev = cur)
            cur = cur.next

        while head :
            if head.val in "-+*/" :
                first = int(head.prev.val)
                second = int(head.prev.prev.val)
                if head.val == '+' :
                    res = first + second
                elif head.val == '*' :
                    res = first * second
                elif head.val == '-' :
                    res = second - first
                else :
                    res = int(second / first)
                head.val = str(res)
                head.prev = head.prev.prev.prev
                if head.prev :
                    head.prev.next = head

            ans = int(head.val)
            head = head.next

        return ans
