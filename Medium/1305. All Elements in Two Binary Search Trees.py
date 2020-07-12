# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        arr1, arr2, answer = [], [], []

        def dfs(node, arr):
            if not node:
                return
            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)

        dfs(root1, arr1)
        dfs(root2, arr2)
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                answer.append(arr1[i])
                i += 1
            else:
                answer.append(arr2[j])
                j += 1

        while i < len(arr1):
            answer.append(arr1[i])
            i += 1

        while j < len(arr2):
            answer.append(arr2[j])
            j += 1

        return answer
