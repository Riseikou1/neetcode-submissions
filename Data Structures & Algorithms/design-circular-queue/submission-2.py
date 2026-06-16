class Node :
    def __init__(self, val = 0, next = None) :
        self.val = val
        self.next = next

class MyCircularQueue:
    def __init__(self, k: int):
        self.cap = k
        self.left = Node()
        self.right = self.left

    def enQueue(self, value: int) -> bool:  # insert before tail. set to right.
        if self.isFull() : return False

        node = Node(value)
        self.right.next = node
        self.right = node

        self.cap -= 1
        return True

    def deQueue(self) -> bool:  # remove from head.
        if self.isEmpty() : return False

        self.left.next = self.left.next.next
        if self.left.next == None :
            self.right = self.left
        
        self.cap += 1
        return True

    def Front(self) -> int:
        if self.isEmpty() : return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty() : return -1
        return self.right.val

    def isEmpty(self) -> bool:
        return not self.left.next

    def isFull(self) -> bool:
        return not self.cap

