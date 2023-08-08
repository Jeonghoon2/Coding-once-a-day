# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def getTargetCopy(self, original, cloned, target):
        d = deque()
        d.append(original)
        visit = []
        visit.append((cloned))

        while d:
            cur_node = d.popleft()


bt = TreeNode(7)
bt.left = TreeNode(4)
bt.right = TreeNode(3)
bt.right.left = TreeNode(6)
bt.right.right = TreeNode(19)
