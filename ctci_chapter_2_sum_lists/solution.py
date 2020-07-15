# sum lists
# you have two numbers represented by a linked list, where each node contains a single digit, the digts are stored
# in reverse order


# use sentinel node for the headpointer
# go through both linked lists
# add together
# store the carry
# carry it over
# if one list ends early
# continue iterate through the rest
# add carry where necesary

def sum_lists(l1, l2):

    # create sentinel node
    return_head = ListNode()
    p1 = return_head
    carry = 0

    while l1 and l2:
        count = l1.val + l2.val + carry

        if count >= 10:
            carry = 1
            new_val = count % 10
        else:
            new_val = count
            carry = 0
        return_head.next = ListNode(new_val)
        return_head = return_head.next
        l1 = l1.next
        l2 = l2.next 

    while l1:
        new_val = l1.val + carry
        if new_val >= 10:
            carry = 1
            new_val = new_val%10
        else:
            carry = 0
        return_head.next = ListNode(new_val)
        return_head = return_head.next
        l1 = l1.next
    while l2:
        new_val = l2.val + carry
        if new_val >= 10:
            carry = 1
            new_val = new_val%10
        else:
            carry = 0
        return_head.next = ListNode(new_val)
        return_head = return_head.next
        l2 = l2.next
    if carry == 1:
        return_head.next = ListNode(1)

    return p1.next

# O(N), O(N)


# add it recusively
# find the where both meet
# add zeroes to the shorter list to match length
# add recursively 




def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def add_zeroes(head, num_zero):
    count = 1
    new_h = ListNode()
    p_h = new_h 
    while count < num_zero:
        new_h.next = ListNode()
        new_h = new_h.next 
        count += 1
    new_h.next = head
    return p_h    


def sum_lists(l1, l2):
    leng_1 = length(l1)
    leng_2 = length(l2)

    if leng_1 < leng_2:
        l1 = add_zeroes(l1, leng_2-leng_1)
    elif leng_1 > leng_2:
        l2 = add_zeroes(l2, leng_1-leng_2)

    
    





























        
    
     
