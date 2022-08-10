# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

# My solution 

def highest_and_low(numbers):
    nums = [int(i) for i in numbers.split( )]
    return f"{max(nums)} {min(nums)}"

numbers = ("1 2 -3 4 5") # -> 5 -3
print(highest_and_low(numbers))

