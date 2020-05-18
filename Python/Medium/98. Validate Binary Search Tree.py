# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, left, right):
            if root is None:
                return True

            if root.val <= left or root.val >= right:
                return False

            if not helper(root.left, left, root.val):
                return False

            if not helper(root.right, root.val, right):
                return False

            return True

        return helper(root, float('-inf'), float('inf'))


# Iterative Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = []
        stack.append((root, (float('-inf'), float('inf'))))
        while stack:
            item = stack.pop()
            node = item[0]
            left = item[1][0]
            right = item[1][1]

            if node is None:
                continue
            elif node.val <= left or node.val >= right:
                return False
            else:
                stack.append((node.left, (left, node.val)))
                stack.append((node.right, (node.val, right)))

        return True
