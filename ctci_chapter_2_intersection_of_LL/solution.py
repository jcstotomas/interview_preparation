# intersection of linked list

# determine if the two lists intersect. return the intersecting node

# 1 2 3 4 5 6
# 0 9 8 4 5 6

# add zeroes to the shortest one
# count until they are the same length
# once you find the start of both the same length, iterate through the
# linked lists and check for the same "reference"


def get_length(head):
    count = 0
    while head:
        count += 1
        head = head.next

    return count 

def find_intersection(h1, h2):
    count1 = get_length(h1)
    count2 = get_length(h2)
    p1 = h1
    p2 = h2 
    diff = abs(count1-count2)
    counter = 0
    if count1 > count2:
        while counter < diff:
            h1 = h1.next
            counter += 1
    elif count2> count1:
        while counter < diff:
            h2 = h2.next
            counter += 1

    while p1 and p2:
        if p1 == p2:
            return p1
        p1=p1.next
        p2=p2.next

    return None
    
