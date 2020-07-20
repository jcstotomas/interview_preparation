# in order successor ii

# if right exists but no parent
    # go right once then go left until none

# while still ni the right subtree, get parent


# get position of current node
    # compare parent and current node

# if position is left, and parent exists, return its parent

# if position is right, then check if node.right exists
    # if it does exist, go right once, then left until u hit none

    # if right does not exist, then go up until you are the left
        # if never left then return None


def inorderSuccessor(node):

    right = False
    left = False
    if node.parent:
        if node.parent.left == node:
            left = True
        elif node.parent.right == node:
            right = True
    if node.right:
        p_tree = node.right
        while p_tree.left:
            p_tree=p_tree.left

        return p_tree
    if node.parent and left:
        return node.parent



    if node.parent and right:
        p_parent = node.parent
        left_p = False
        while p_parent.parent and not left:
            if p_parent == p_parent.parent.left:
                return p_parent.parent
            p_parent = p_parent.parent

    return None
        

        
        
