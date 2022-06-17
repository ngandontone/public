# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            
            if not root:
                return [True, 0]
        
            right = dfs(root.right)
            left = dfs(root.left)
        
            balanced = abs(right[1]-left[1]) <= 1 and right[0] and left[0]
        
            return [balanced, 1 + max(right[1],left[1])]
    
        return dfs(root)[0]