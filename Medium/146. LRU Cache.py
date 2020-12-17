class Node:
    def __init__(self, k = None, v = None):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maxCapacity = capacity
        self.currCapacity = 0
        self.dict = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToFront(self, node):
        newSecondNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = newSecondNode
        newSecondNode.prev = node

    def moveToFront(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.addToFront(node)

    def removeLRU(self):
        oldNode = self.tail.prev
        oldNode.prev.next = self.tail
        self.tail.prev = oldNode.prev
        oldNode.next = None
        oldNode.prev = None
        self.dict.pop(oldNode.key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        item = self.dict.get(key, None)
        if item is not None:
            self.moveToFront(item)
            return item.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.dict:
            newNode = Node(key, value)
            if self.currCapacity >= self.maxCapacity:
                self.removeLRU()
            self.dict[key] = newNode
            self.addToFront(newNode)
            self.currCapacity += 1
        else:
            self.dict[key].val = value
            self.moveToFront(self.dict[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
