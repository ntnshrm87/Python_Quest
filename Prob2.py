# Prob 2:

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(2,[1,2,3])
f(3)
f(4)

# Solution:
# [0, 1]
# [1, 2, 3, 0, 1]
# [0, 1, 0, 1, 4]
# [0, 1, 0, 1, 4, 0, 1, 4, 9]

# Reference:
# The new default list is created only once when the function is defined, and that same list
# is then used subsequently whenever f is invoked without a list argument being specified.
# This is because expressions in default arguments are calculated when the function is defined,
# not when it’s called.

# A revised implementation of function can be made to get the appropriate output.
'''
def f(x,l=None):
    if l is None:
        l = []
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(2,[1,2,3])
f(3)
f(4)
'''
# Solution:
# [0, 1]
# [1, 2, 3, 0, 1]
# [0, 1, 4]
# [0, 1, 4, 9]
