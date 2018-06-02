# Prob 6

list_a = ['Raman', 'Bose', 'Bhatt', 'Modi']

# Case 1
print(list_a[10:])

# Case 2
try:
    print(list_a[10])
except IndexError as e:
    print("Error is: ", e)

# Case 3
print(list_a[:-10])

# Solution:
# []
# Error is:  list index out of range
# []

# Reference:
# Its really a tricky one
# The problem is if you are accessing a particular value
# whose index is out of range from the list, error will be
# shown. However, if you are trying to access the list slice
# in either lef or right side exceeding the number of members
# in the list will simply result in empty list.
