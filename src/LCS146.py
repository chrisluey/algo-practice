class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
             
    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self._remove(n)
            self._add(n)
            return n.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            n = self.d[key]
            self._remove(n)
            # n.val = value
            # self._add(n)
        elif len(self.d.keys()) >= self.capacity:
            lru = self.head.next
            self._remove(lru)
            self.d.pop(lru.key)
        newNode = Node(key, value)
        self.d[key] = newNode
        self._add(newNode)
            
    def _add(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail
        
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)