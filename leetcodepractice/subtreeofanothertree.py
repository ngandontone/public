# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sameTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    
    left = sameTree(root1.left, root2.left)
    right = sameTree(root1.right, root2.right)
    
    return True if left and right else False
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if sameTree(root,subRoot):
            return True
        
        left_subtree = self.isSubtree(root.left,subRoot)
        right_subtree = self.isSubtree(root.right,subRoot)
        
        return left_subtree or right_subtree