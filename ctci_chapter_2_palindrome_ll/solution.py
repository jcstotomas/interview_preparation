# linked list palindrome

# 1 2 2 1 -> true

# 1 3 1 1 -> false
# 1 2 1 2 1

#  plan
# find the middle of the linked lsit
# reverse first half
# iterate through both 

def linked_list_palindrome(head):

    # find middle of linked list

    p1 = head
    p2 = head

    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next


    # reverse second half

    previous = None
    next = None
    p_middle = p1

    while p_middle:
        next = p_middle.next
        p_middle.next = previous
        previous = p_middle
        p_middle = next

    end_of_list = previous

    while end_of_list:
        if end_of_list.val != head.val:
            return False
        end_of_list = end_of_list.next
        head = head.next

    return True
    

    
