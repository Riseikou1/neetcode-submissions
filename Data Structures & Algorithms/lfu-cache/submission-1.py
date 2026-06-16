class Node:
    def __init__(self, key = None, val = None, next = None, prev = None):
        self.key = key
        self.val = val
        self.freq = 1

class DLinkedList:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return None
        if node is None:
            node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.nodes = {}  # key -> Node
        self.freqs = defaultdict(DLinkedList)  # freq -> DLinkedList

    def _update(self, node):
        freq = node.freq
        self.freqs[freq].pop(node)
        if freq == self.min_freq and self.freqs[freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        self.freqs[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0 : return

        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._update(node)
        else:
            if self.size == self.capacity:
                to_remove = self.freqs[self.min_freq].pop()
                del self.nodes[to_remove.key]
                self.size -= 1

            new_node = Node(key, value)
            self.nodes[key] = new_node
            self.freqs[1].append(new_node)
            self.min_freq = 1
            self.size += 1
