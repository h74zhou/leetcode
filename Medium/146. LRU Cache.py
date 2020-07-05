class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.count = 0

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertFront(self, node):
        currHead = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = currHead
        currHead.prev = node

    def moveToFront(self, node):
        self.removeNode(node)
        self.insertFront(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.moveToFront(self.cache[key])
        return self.cache[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key].value = value
            self.moveToFront(self.cache[key])
        else:
            newNode = Node(key, value)
            if self.count + 1 > self.capacity:
                self.cache.pop(self.tail.prev.key, None)
                self.removeNode(self.tail.prev)
            else:
                self.count += 1
            self.insertFront(newNode)
            self.cache[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
