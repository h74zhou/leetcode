import heapq

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        queue = [root]
        arr = []
        while queue:
            temp = []
            for node in queue:
                arr.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp[:]

        heapq.heapify(arr)
        kthSmallest = 0
        for i in range(k):
            kthSmallest = heapq.heappop(arr)

        return kthSmallest
