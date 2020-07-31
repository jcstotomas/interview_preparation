# search in rotated array


#  7 8 9 1 2 3 4 56 
# 1 2 3 4  5 6 7 8

# binary search
# modified binary search

# check left most and right most
# if desired value is greater than left and less than mid
    # binary search the left side
# if desired value is less than right and greater than mid
    # binary search the right side
# if middle == value
    # return middle


def modified_binary_search(a, start, end, target):
    mid = start  + (end-start) // 2
    mid_value = a[mid]
    print("a")
    if mid_value == target:
        return mid
    elif mid_value >= a[start] and target >= a[start] and target < mid_value:
        return modified_binary_search(a, start, mid-1, target)
    elif mid_value >= a[start]:
          return modeified_binary_search(a,mid+1, end,target)
    elif mid_value < a[start] and target <= a[end] and target > mid_value:
        return modified_binary_search(a, mid+1, end, target)
    elif mid_value < a[start]:
        return modified_binary_search(a, start, mid-1, target)
    return -1


array = [7,8,9,1,2,3,4,5,6]

print(modified_binary_search(array, 0, len(array)-1, 7))
    
    

