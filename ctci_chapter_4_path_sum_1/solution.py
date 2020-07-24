class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # recursively subtract 
        
        if not root:
            return False
        if not root.left and not root.right and sum-root.val == 0:
            return True
        if not root.left and not root.right and sum-root.val != 0:
            return False
        left, right = False, False
        if root.left:
            left = self.hasPathSum(root.left, sum-root.val)
        if root.right:
            right = self.hasPathSum(root.right, sum-root.val)
        
        return left or right
        
