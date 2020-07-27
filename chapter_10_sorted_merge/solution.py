# sorted merge

#You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.

# merge sort

# 1 2 3 4 5
# 6 7 8

# 1 5 6 7 8
# 2 3 9
# 9 8 7 5 5 3 2 1

# plan
# take the both lists
# iterate through them
# if b is less than current a
# push

# new way
# add from back to front
# keep track


def sorted_merge(a1, a2):
    cur_index = len(a1)-1
    a1_end = len(a1) - len(a2) - 1
    a2_end = len(a2) -1
    if len(a2) == 0:
        return a1
    while cur_index >= 0:
        if a1_end != -1 and (a1[a1_end] >= a2[a2_end] or a2_end == -1):
            a1[cur_index] = a1[a1_end]
            a1_end-=1
        elif a2[a2_end] > a1[a1_end] or a1_end == -1:
            a1[cur_index] = a2[a2_end]
            a2_end-=1
        cur_index -= 1

    return a1

one = [1,2,3,0,0,0]
two = [4,5,6]

print(sorted_merge(one,two))



        
