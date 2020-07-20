# check balanced binary search tree
# implement a function to check if a binary search tree is balanced

# balanced is that heights of two subtrees of any node never differs by more than one


# plan

# recursively count the heights of left and right nodes
# then do a comparison, if difference greater than one, then return False

def solution():
    not_balanced = True

    def check_balanced(root):
        if root == None:
            return 0

        if root.left:
            left_height = check_balanced(root.left) + 1

        if root.right:
            right_height = check_balanced(root.right) + 1

        if abs(right_height - left_height) > 1:
            not_balanced = False

        return max(root.left,root.right)

    
