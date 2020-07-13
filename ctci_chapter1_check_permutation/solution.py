# check permutation


# "asd", "das" -> true
# "asdd", "das" -> false


# hash set/sorting problem

# sorting
# sort both
# if lengths are not the same->return false
# else, if each index are not the same then return false

# count all the letters in each, then do a comparison 

def check_permutation(s1, s2):
    # sorting solution

    if len(s1) != len(s2):return False
    
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    for i in range(len(s1)):
        if sorted_s1[i] != sorted_s1[i]:
            return False


    return True


# run tim e is O(N LOG N) due to sorting
# O(1) space -> dependent on if sorting allocates a new string

a = "ads"
b = "dass"
assert(check_permutation(a,b) == False)

    
