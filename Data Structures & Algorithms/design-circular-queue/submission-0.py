class Node :
    def __init__(self, val = 0, prev = None, next = None) :
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:
    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool: 
        if self.isFull() :
            return False

        node = Node(value,self.tail.prev, self.tail) 
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() : return False

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty() :
            return self.head.next.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty() :
            return self.tail.prev.val
        return -1

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def isFull(self) -> bool:
        return self.cap == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()