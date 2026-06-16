class Node :
    def __init__(self, key = None, val = None, prev = None, next = None) :
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.cap = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def delete(self, node) :
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def add(self, node) :
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def update(self, node) :
        self.delete(node)
        self.add(node)

    def get(self, key: int) -> int:
        if key not in self.hashmap :
            return -1
        self.update(self.hashmap[key])
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap :
            node = Node(key, value)
            self.hashmap[key] = node
            self.add(node)
        else :
            self.update(self.hashmap[key])
            self.hashmap[key].val = value
        
        if self.size > self.cap :
            node_to_del = self.head.next
            self.delete(node_to_del)
            del self.hashmap[node_to_del.key]

