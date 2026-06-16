class Node :
    def __init__(self, key = None, val = None) :
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail

    def remove(self, node) : # from head.
        prev, nxt = node.prev, node.next
        nxt.prev = prev
        prev.next = nxt

    def insert(self, node) : # to tail.
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache :
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache : 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap :
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
