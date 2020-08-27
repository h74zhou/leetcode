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
        stack, curr = [root], root.left

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                popped = stack.pop()
                answer.append(popped.val)
                curr = popped.right
        return answer
