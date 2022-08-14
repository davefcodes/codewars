# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.


def remove_char(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return "".join(s)

s = "hello" # -> output "ello"
s = "eloquent" # -> output "loquent"

print(remove_char(s))




