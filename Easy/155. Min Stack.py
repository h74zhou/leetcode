class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0 and len(self.minstack) == 0:
            self.minstack.append(x)
        else:
            if self.minstack[-1] >= x:
                self.minstack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        popped = self.stack.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()