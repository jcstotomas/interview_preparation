## is unique
# implement an algorithm to determine if a string has all unique characters

# input -> string
# output -> boolean

# "aaa" -> false
# " abc"->return true

# hash table/set to track

# create a set for tracking characters
# for each character in the string, add it into the set
# if the chracter is in the set, return false
# return false at the end

def is_unique(string: str) -> bool:
    # define the set 
    seen = set()
    # iterate through the string
    for s in string:
        if s in seen:
            return False
        else:
            seen.add(s)
    # returns true if any of the characters are not seen 
    return True

# O(N) -> n being the characters in the string
# O(N) space -> n being the set given
# pros -> fast, cons -> extra space

#Follow up -> no extra space
# sort
# after sorting, check to see if next value is the same, go by pairs
# start from index 1, check previous, if they are == then return False
# else return True once iterated through teh list 
def is_unique2(string):
    # sort
    sorted_string = sorted(string)
    if len(string) <= 1:
        return True 
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            return False
    return True
    # this runs in O(N) and O(1) space assuming sorting is efficient
#test cases
test1 = ""
test2 = " "
test3 = "aaaaa"
test4 = "abcdd"
test5 = "abcdefghijklm123456788"
test6 = "abcdefghijklm12345678"
assert(is_unique2(test1) == True)
assert(is_unique2(test2) == True)
assert(is_unique2(test3) == False)
assert(is_unique2(test6) == True)




