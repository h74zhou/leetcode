# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def depth(self, root):

        if root is None:
            return 0

        leftHeight = self.depth(root.left) + 1
        rightHeight = self.depth(root.right) + 1

        return max(leftHeight, rightHeight)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = []
        queue.append(root)

        if root is None:
            return True

        while len(queue) != 0:
            node = queue.pop()
            if (node.left is not None):
                leftHeight = self.depth(node.left)
            else:
                leftHeight = 0

            if (node.right is not None):
                rightHeight = self.depth(node.right)
            else:
                rightHeight = 0

            if abs(rightHeight - leftHeight) > 1:
                return False

            if (node.left is not None):
                queue.append(node.left)

            if (node.right is not None):
                queue.append(node.right)

        return True
