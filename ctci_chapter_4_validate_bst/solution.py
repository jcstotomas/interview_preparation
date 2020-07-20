# validate binary search tree

# implement a function to check if it is a BST

# do a in order traversal and check if each value is less than that node

# plan

# recursively solve both left and right

# left subtree must have all be less than the parent node
# right subtree must have all be greater than parent node

# in order traversal

# cehck and see if last value is greater than the last


# track the last seen value using an in order traversal
# if the last value is not in ascending order, then return out of it


#left, middle, right
last_value = -float('inf')
is_bst = []
def validate_bst(root):

    if root:
        validate_bst(root.left)
        is_bst.append(root.val)
        validate_bst(root.right)
        

for i in range(1,len(is_bst)):
    if is_bst[i-1] > is_bst[i]:
        return False
    
    
