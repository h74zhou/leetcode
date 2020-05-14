# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.answer = []

        def dfs(root, currLst, currSum):
            if not root:
                return

            currLst.append(root.val)
            currSum += root.val

            if not root.left and not root.right and currSum == sum:
                self.answer.append(currLst)

            dfs(root.left, currLst[:], currSum)
            dfs(root.right, currLst[:], currSum)

        dfs(root, [], 0)
        return self.answer
