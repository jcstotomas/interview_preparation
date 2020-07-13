# palindrome permutation



# tact coa -> taco cat
# ignore casing, non letter characters

# characters must be an even amount besides one if length is odd
# ababab
# if character length is even -> one must be odd
# if character length is odd -> only one can be odd 
# aba, abba, abbba, abcba, aabbaa
# if count is even then, none can be odd 

# aa bb
# count the number of alpha num characters
# for each count, check constraints

def length(s):
    count = 0
    for i in s:
        if i.isalnum():
            count += 1
    return count 

def palindrome_permutation(s1):

    l = length(s1)
    character_counts = {}
    for i in s1:
        if i.isalnum():
            if i in character_counts:
                character_counts[i] += 1
            else:
                character_counts[i] = 1
    is_even = False
    is_odd = False
    if l % 2 == 0:
        is_even = True
    else:
        is_odd = False
    print(character_counts.values())
    for i in character_counts.values():
        print(i)
        if i % 2 != 0 and is_even:
            return False
        elif i % 2 != 0 and not is_odd:
            is_odd = True

        elif i % 2 != 0 and is_odd:
            return False
    return True

a = "ab"

print(palindrome_permutation(a))
    
# O(N) space, O(N) time -> N being the number of characters in the string 
# 



