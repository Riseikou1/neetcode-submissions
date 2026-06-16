class Node :
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache :  # head.next will be lru node.
            self.helper(self.cache[key])           
            return self.cache[key].val
        else : 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value

            cur = self.cache[key]
            self.helper(cur)

        else :
            node = Node(key,value)
            self.cache[key] = node
            tmp = self.tail.prev
            node.prev = tmp
            node.next = self.tail
            tmp.next = node
            self.tail.prev = node
        
        # deleting should happen. 2nd step
        # delete head.next

        if len(self.cache) > self.cap :
            node_to_be_deleted = self.head.next
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            del self.cache[node_to_be_deleted.key]

    def helper(self,cur):
            prev = cur.prev
            cur_next = cur.next
            prev.next = cur_next
            cur_next.prev = prev

            tail_prev = self.tail.prev
            tail_prev.next = cur
            cur.prev = tail_prev
            cur.next = self.tail
            self.tail.prev = cur
