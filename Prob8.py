# Prob 8:

# Question: Is Python 'call-by-value' or 'call-by-reference'

# Example:
x = 3456
print(id(x))

y = 3456
print(id(y))

x = 1234
print(id(x))

# Answer: NEITHER. Its just binding of a name to an object.

# Solution:
# 140397975727952
# 140397975727952
# 140397975785328

# Reference:
# The id number is a conceptual memory address which came exactly
# similar for first two addresses of x and y. This means x and y
# are just labels to that particular memory location. We have
# changed the value of x assignment, and the id number got
# changed. This means that if we refer to the memory returned
# previously we can get the previous value of x. Its not going
# to be deleted/overwritten like that in traditional C/C++.



