# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        answer = []
        if not root:
            return answer

        q, count = [root], 2

        while q:
            currLevel, nextLevel = [], []
            for node in q:
                if count % 2 == 0:
                    currLevel.append(node.val)
                else:
                    currLevel.insert(0, node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            count += 1
            answer.append(currLevel[:])
            q = nextLevel[:]

        return answer
