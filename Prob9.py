# Prob 9:

# Question: What are immutable and mutable data types

# Example:
l_a = ['a', 'b', 'c', 'd']
t_a = ('a', 'b', 'c', 'd', l_a)

print("l_a is: ", type(l_a))
print("t_a is: ", type(t_a))

try:
    t_a.append('e')
except AttributeError as e:
    print ("Error is: ",e)

t_a[4].append('e')
print(t_a)

# Answer:
# Immutable: does not exhibit time-varying behavior e.g. tuple
# Mutable: exhibit time varying behavior e.g. list

# Solution:
# l_a is:  <class 'list'>
# t_a is:  <class 'tuple'>
# Error is:  'tuple' object has no attribute 'append'
# ('a', 'b', 'c', 'd', ['a', 'b', 'c', 'd', 'e'])

# Reference:
# Tuple being immutable can't be modified and we can observe
# that an attribute error came. While, List is mutable and can
# be modified. Here a special case is described where a list is
# present inside the tuple and hence we are able to modify it.
# Its all because of binding in Python.

