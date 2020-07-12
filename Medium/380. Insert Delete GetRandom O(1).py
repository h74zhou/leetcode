import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.arr.append(val)
            self.dict[val] = len(self.arr) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False

        valIndex = self.dict[val]
        lastIndex = len(self.arr) - 1
        last = self.arr[lastIndex]
        self.arr[valIndex], self.arr[lastIndex] = self.arr[lastIndex], self.arr[valIndex]
        self.dict[last] = valIndex
        self.arr.pop()
        self.dict.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randomIndex = random.randint(0, len(self.arr) - 1)
        return self.arr[randomIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
