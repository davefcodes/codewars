# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0


# My Solution
def make_negative(number):
    return -abs(number)


#test case
number = -5
number = 0
print(make_negative(number))
print(make_negative(number))
