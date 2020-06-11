# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        currSum = root.val
        queue = [root]

        while queue:
            temp = []
            tempSum = 0
            for node in queue:
                tempSum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            currSum = tempSum
            queue = temp[:]

        return currSum
