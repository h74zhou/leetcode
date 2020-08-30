# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        if not root:
            return answer

        stack = []

        while stack or root is not None:
            if root:
                stack.append(root)
                root = root.left
            else:
                last = stack.pop()
                answer.append(last.val)
                root = last.right

        return answer
