import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            self.d[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        arrIndex = self.d.get(val)
        if arrIndex is not None:
            # swap the element to the last index of the array
            self.arr[arrIndex], self.arr[-1] = self.arr[-1], self.arr[arrIndex]
            # update the non-removed index
            self.d[self.arr[arrIndex]] = arrIndex
            # pop the last element from arr
            self.arr.pop()
            # remove from dictionary
            self.d.pop(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.arr[random.randint(0, len(self.arr) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
