class ListNode :
    def __init__(self, val = 0, next = None, prev = None) :
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList :
    def __init__(self) :
        self.map = {}
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def length(self) :
        return len(self.map)

    def pop(self, val) :
        if val in self.map :
            node = self.map[val]
            prv, nxt = node.prev, node.next
            prv.next = nxt
            nxt.prev = prv
            self.map.pop(val, None)

    def popLeft(self) -> int :
        res = self.head.next.val
        self.pop(res)
        return res

    def pushRight(self, val) :
        node = ListNode(val, self.tail, self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        self.map[val] = node

    def update(self, val) :
        self.pop(val)
        self.pushRight(val)

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.lfuCnt = 0
        self.countMap = defaultdict(int)
        self.valMap = {}
        self.ListMap = defaultdict(LinkedList)

    def counter(self, key) :
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.ListMap[cnt].pop(key)
        self.ListMap[cnt + 1].pushRight(key)

        if cnt == self.lfuCnt and self.ListMap[cnt].length() == 0 :
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap : return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.valMap :
            if len(self.valMap) == self.cap : 
                res = self.ListMap[self.lfuCnt].popLeft()
                self.valMap.pop(res)
                self.countMap.pop(res)

            self.valMap[key] = value
            self.countMap[key] = 1
            self.ListMap[1].pushRight(key)
            self.lfuCnt = 1

        else :
            self.counter(key)
            self.valMap[key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)