# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        depth = 0
        if root is None:
            return depth
        q = deque()
        q.append((root, 1))

        while q:
            cur_node, cur_depth = q.popleft()

            if cur_depth > depth:
                depth = cur_depth

            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))
        return depth


root = TreeNode(val=3)
root.left = TreeNode(val=9)
root.right = TreeNode(val=20)
root.right.left = TreeNode(val=15)
root.right.right = TreeNode(val=7)

print(Solution().maxDepth(root))
