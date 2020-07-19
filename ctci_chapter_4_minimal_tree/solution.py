# minimal tree
# given a sorted increasing array
# write an algorithm to create a binary tree with minimum height

# 1 2 3 4 5 6 7 8

# plan find the mid point
# recursively find the mid point
# each midpoint will be the child depending on its size
# recursively slice the list

# first find the first mid point for the root node
# then slice two sides in half
# find mid ponit again and set l and r to this value

class TreeNode:
    def __init__(self, val, right=None,left=None):
        self.val = val
        self.right = right
        self.left =left 

def create_binary_search_tree(array):
    # find mid point
    if len(array) == 1:
        return TreeNode(array[0])

    mid_point = 0 + (len(array) - 0) // 2

    mid_point_node = TreeNode(array[mid_point])

    mid_point_node.left = create_binary_search_tree(array[0:mid_point])
    mid_point_node.right = create_binary_search_tree(array[mid_point+1:r])


    return mid_point_node
