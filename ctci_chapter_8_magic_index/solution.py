# a magic index is in an array
# such tht A[i] == i

# obvious approach
# linear scan
# 1 1 1 2 2 3 3

def magic_index(array, left, right):
    if left <= right:
        mid = left + (right - left) // 2
        
        if array[mid] == mid:
            return mid


        if array[mid] < mid:
            return magic_index(array, mid+1, right)


        elif array[mid] > mid:
            return magic_index(array, left, mid-1)


    return None
a = [-1, 0, 1, 2, 4, 10]
print(magic_index(a, 0,len(a)-1))
