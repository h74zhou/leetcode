class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.hash:
            self.hash[key] = 1


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hash:
            self.hash.pop(key, 'None')

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hash


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
