## list of depths

# given a binary tree, design an algorithm
# that creates a liniked list of all the nodes at each depth


# find depth
    # recursively count each side and take the max of each side

# after finding depth, create list of linked lists of all the depths

# isntead of level order traversal, do a normal traversal and just pass the level you are on 

def find_depth(root):
    if root == None:
        return 0

    if root.left:
        left = find_depth(root.left) + 1
    if root.right:
        right = find_depth(root.right) + 1

    return max(left,right)


def create_list

def list_of_depths(root):
    list_of_nodes = [
