# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    stack = []
    emptyRoot = False

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root is None:
            self.emptyRoot = True
            return

        def dfs(root):
            if root is None:
                return None

            dfs(root.left)
            self.stack.append(root.val)
            dfs(root.right)

        dfs(root)
        self.stack.reverse()

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        last = self.stack.pop()
        return last

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.emptyRoot or len(self.stack) == 0:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
