# check subtree
# t1 and t2 are large binary tree
# t1 is much bigger create an algorithm



# plan

# find the node where they are equal to each other

# if nodes are the same return True
# if they are not return False

def compare_trees(t1,t2):
    if t1 == None and t2:
        return False
    if t2 == None and t1:
        return False
    if t1 == None and t2 == None:
        return True
    left = compare_trees(t1.left, t2.left)
    right = compare_trees(t1.right, t2.right)
    if t1.val != t2.val:
        return False
    if t1.val == t2.val:
        return left and right and True


def search_for_node(t1, t2):
    if t1 == t2:
        return t1
    left, right = None, None
    if t1.left:
        left = search_for_nodes(t1.left, t2)
    if t1.right:
        right = search_for_nodes(t1.right, t2)

    if t1 == None:
        return None

    if left:
        return left
    if right:
        return right
    return None
        

def check_subtrees(t1, t2):
    
