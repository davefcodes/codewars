#Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# My Solution:

def reversed(string):
    # Pythonic Solution
    # return string[::-1]
    
    newstring = ''
    
    for char in string:
        newstring = char + newstring
    return newstring

string = 'world'
print(reversed(string))


