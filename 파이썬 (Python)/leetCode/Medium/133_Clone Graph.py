# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        visit = []







print(Solution().cloneGraph([[2, 4], [1, 3], [2, 4], [1, 3]]))
