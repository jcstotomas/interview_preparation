# one away

# there are three types of edits taht can be performed on strings:
# insert, remove, replace a character
# given two strings writea function to check if they are one or 0 edits away


# pale -> ple is true
# pales -> pale is true
# pale -> bale is true
# pale -> bake is false


# hashtable,set -> tracking characters?

# iterate through and find the missing characters

# get shorter one, and find first character and then do matching

# same length -> just check each subsequent character


def same_length(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count <= 1

def one_away(s1, s2):
    # check for length
    if len(s1) == len(s2):
        return same_length(s1,s2)

    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) < len(s2):
        shortest = s1
        longer = s2
    else:
        shortest = s2
        longer = s1 
    longer_index = 0
    error_count = 0
    short_len = 0
    while short_len < len(shortest) and longer_index < len(longer):
        if shortest[short_len] != longer[longer_index]:
            error_count += 1
            longer_index += 1
        else:
            longer_index += 1
            short_len += 1
    return error_count < 2


# test cases


print(one_away("pale", "pale"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("a",  ""))



