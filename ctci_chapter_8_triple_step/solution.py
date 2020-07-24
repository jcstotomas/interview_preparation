# a child  running up a staircase with n steps can hop either 1,2 or 3 steps up
 # the stairs
# count the number of possible ways for the child to run up the stairs

# 4
# 1 + 1 + 1 + 1
# 1 + 2 + 1
# 1 + 3

# recursive solution

# if sum > value, then return
# if sum == 0, add to it

def recursion(n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    one = recursion(n-1)
    two = recursion(n-2)
    #three = recursion(n-3)

    return one + two# + three

# memoized/iterative solution

def optimized(n):
    #work backwards
    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 2
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[-1]
