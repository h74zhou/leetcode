# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        maxLevel, currLevel = 1, 1
        maxLevelSum = root.val

        while queue:
            temp = []
            levelSum = 0
            for node in queue:
                levelSum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if levelSum > maxLevelSum:
                maxLevelSum = levelSum
                maxLevel = currLevel
            currLevel += 1
            queue = temp[:]

        return maxLevel
