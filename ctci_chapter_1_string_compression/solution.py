# basic string compression,

# aabcccccaaa -> a2b1c5a3


# count the number of characters seen
# if one is different then add that count
# no need for extra space


# iterate through the string
# keep track of last seen character
# keep track of count of last seen
# if you see the same character, add 1
# if you see different character, add last count and character to the new string 

def string_compression(s1):
    last_character = s1[0]
    count = 1

    if len(s1) == 1:
        return s1 + '1'
    if len(s1) == "":
        return ""
    return_string = ""
    for i in range(1, len(s1)):
        cur_char = s1[i]
        if cur_char == last_character:
            count += 1
        else:
            return_string += last_character + str(count)
            last_character = cur_char
            count = 1

    return return_string + last_character + str(count)


print(string_compression("aab"))


    
