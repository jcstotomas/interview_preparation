# write a method to srot an array of strings
# so that all anagrams are next to each other


# ["the", "as", "po", "op", "sa", "eht"]
# -> [["the", "eht", "as", "po",

# plan
# sort anagrams by letter
# store anagrams in a hash table

# if the sorted stringi s in the table, insert into dictionary


def group_anagrams(list_of_anagrams):
    # store it into a dictionary

    seen_anagrams = {}

    for s in list_of_anagrams:
        sorted_string = "".join(sorted(s))
    
        if sorted_string in seen_anagrams:
            seen_anagrams[sorted_string].append(s)
        else:
            seen_anagrams[sorted_string] =[s]


    return_value = []
    for i in seen_anagrams.values():
        return_value.append(i)


    return return_value
a = ["the", "as", "po", "op", "sa", "eht"]
print(group_anagrams(a))
