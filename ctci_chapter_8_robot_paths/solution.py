# robot is located at the top left corner
# with an m x n grid
# robot can only move down or right at any point in time

# the robot is trying to reach the bottom-right corner of the grid

# how many unique possible paths are there


# recursion

# for each path go down and righht
# if it reaches the bottom or the right most
# only go in one direction
# m x n
# 0 - m, 0 - n non inclusive

def robot_paths(m,n):
    print(m,n)
    if m == 1 and n == 1:
        return 1
    left, up = 0,0
    if m > 0:
        left = robot_paths(m-1, n)

    if n > 0:
        up = robot_paths(m,n-1)

    return left + up


def robot_paths_memoized(m,n):
    # create an m x n matrix
    # take values from previous and add it together
    # memoized solution

    matrix =  [[0 for x in range(m)] for j in range(n)]
    # iterate 
    if m == 1 and n == 1:
        return 1 
    # row by row, first row is just one
    for i in range(n):
        matrix[i][0] = 1
    for j in range(m):
        matrix[0][j] = 1

    
    for i in range(1,n):
        for j in range(1,m):
            matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
    return matrix[-1][-1]

robot_paths_memoized(7,3)




    
    
