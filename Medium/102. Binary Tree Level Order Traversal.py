# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        answer = []
        if not root:
            return answer

        queue = [root]
        while queue:
            temp = []
            level = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            answer.append(level)
            queue = temp[:]

        return answer
