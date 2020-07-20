# in order successor

#

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # in order traversal
        
        # in order traversal, add it to a list, return next one 
        self.list = []
        def add_to_list(root):
            if root:
                add_to_list(root.left)
                self.list.append(root)
                add_to_list(root.right)
        
        add_to_list(root)
        
        for i in range(len(self.list)):
            cur_node = self.list[i]
            if self.list[i] == p and i+1 != len(self.list):
                return self.list[i+1]
        
        return None
                
