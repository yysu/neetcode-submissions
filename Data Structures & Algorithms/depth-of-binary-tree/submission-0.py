# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_height = self.dfs(root)
        return max_height

    def dfs(self, root):
        if not root:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))