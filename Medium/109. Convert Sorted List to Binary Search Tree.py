# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        li = []
        node = head

        while node:
            li.append(node.val)
            node = node.next

        def operate(left, right):
            if left > right:
                return
            mid = (left + right) / 2
            node = TreeNode()
            node.val = li[mid]
            node.left = operate(left, mid - 1)
            node.right = operate(mid + 1, right)
            return node

        return operate(0, len(li) - 1)
