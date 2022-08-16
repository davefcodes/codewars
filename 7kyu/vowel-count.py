# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.


# My Solution 
def get_count(sentence):
    vowels = 0

    for i in sentence:
        if i in ["a", "e", "i", "o", "u"]:
            vowels += 1
        else:
            pass
    return vowels


sentence = ("a", "e", "i", "o", "u") # result -> count 5
print(get_count(sentence))

