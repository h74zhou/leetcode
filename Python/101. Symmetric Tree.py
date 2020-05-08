# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val == right.val:
            return True and self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left, root.right)


# Iterative Solution
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False

        queue = []
        queue.append(root.right)
        queue.append(root.left)

        while len(queue) > 0:
            temp = []
            while len(queue) > 0:
                first = queue.pop(0)
                second = queue.pop(0)
                if first is None and second is None:
                    continue
                elif first is None or second is None:
                    return False
                elif first.val == second.val:
                    temp.append(first.left)
                    temp.append(second.right)
                    temp.append(first.right)
                    temp.append(second.left)
                elif first.val != second.val:
                    return False
            queue = temp

        return True


