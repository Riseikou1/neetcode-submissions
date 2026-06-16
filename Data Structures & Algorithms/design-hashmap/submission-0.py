class ListNode :
    def __init__(self, key = 0, val = 0, next = None) :
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.size = 10 ** 4 + 1
        self.buckets = [ListNode() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        cur = self.buckets[key % self.size]
        while cur.next :
            if cur.next.key == key :
                cur.next.val = value
                return 
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.buckets[key % self.size]
        while cur.next :
            if cur.next.key == key :
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.buckets[key % self.size]
        while cur.next :
            if cur.next.key == key :
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)