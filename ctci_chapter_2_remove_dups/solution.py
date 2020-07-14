# write code the remove duplicates from an unsorted list


# 3 3 4 5 6 7 0 9

# 3 4 5 6 7 0 9


# plan
# we could use extra space
# check for any existing duplicates and then remove it from there


# use hash set to check for existing node values

# for each value the linkedl ist, add to the hash set
# if value in hash set, set previous to node.next


class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next
def print_ll(head):
    while head:
        print(head.val)
        head = head.next
def remove_duplicates(head):
    # create hash set

    s = set()
    p = head
    previous = None
    while p:
        if p.val not in s:
            s.add(p.val)
            previous = p
        else:
            previous.next = p.next

        p = p.next

    print_ll(head)
    return head


a = ListNode()
b = ListNode()
c = ListNode(2)
d = ListNode(2)
e = ListNode(3)
f = ListNode(4)
g = ListNode(5)


a.next = b
b.next = c
c.next = e
e.next = f
f.next = g
g.next = d
remove_duplicates(a)





        
