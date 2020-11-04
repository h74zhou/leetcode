class Node:
    def __init__(self, k = None, v = None):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {} # key -> Node(key, value)
        self.count = 0

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addFront(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node

    def moveToFront(self, node):
        self.removeNode(node)
        self.addFront(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        possibleNode = self.cache.get(key)
        if possibleNode:
            self.moveToFront(possibleNode)
            return possibleNode.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        existingNode = self.cache.get(key)
        if existingNode:
            self.cache[key].value = value
            self.moveToFront(existingNode)
        else:
            newNode = Node(key, value)
            if self.count + 1 > self.capacity:
                self.cache.pop(self.tail.prev.key)
                self.removeNode(self.tail.prev)
            else:
                self.count += 1
            self.addFront(newNode)
            self.cache[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
