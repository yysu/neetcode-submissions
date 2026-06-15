# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.isSametree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSametree(self, root, another):
        if not root and not another:
            return True
        
        if root and another and root.val == another.val:
            return self.isSametree(root.left, another.left) and self.isSametree(root.right, another.right)
        else:
            return False