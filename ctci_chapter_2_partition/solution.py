# partition

# partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x

# 3 5 7 5 10 2, x = 5
# 3 1 2  5 7 5 8


# allocate two linked lists
# one for values before x
# one for values after x
# have separate pointers for each one to point to their heads
# as you go through each, add corresponding to it, keep track of previous

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def partition_linked_list(head, x):
    # allocate two linked lists

    less = ListNode()
    more = ListNode()
    p_less = less
    p_more = more
    while head:
        if head.val < x:
            less.next = head
            previous_less = less
            less = less.next
        elif head.val >= x:
            more.next = head
            more = more.next
        head = head.next
    more.next=None
    less.next = p_more.next
    return p_less.next

# O(N) -> N being number of elements
# O(N) -> allocate ll of N length
    
