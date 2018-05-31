# Prob 3
def multipliers():
    return [lambda x: i * x for i in range(4)]

print ([m(2) for m in multipliers()])

# Solution:
# [6, 6, 6, 6]

# Reference:
#The reason for this is that Python’s closures are late binding. This means that the values
# of variables used in closures are looked up at the time the inner function is called.
# So as a result, when any of the functions returned by multipliers() are called, the value
# of i is looked up in the surrounding scope at that time. By then, regardless of which
# of the returned functions is called, the for loop has completed and i is left with its
# final value of 3. Therefore, every returned function multiplies the value it is passed by 3,
# so since a value of 2 is passed in the above code, they all return a value of 6 (i.e., 3 x 2).

# Improved Solution: create a closure that binds immediately to its
# arguments by using a default argument
'''
def multipliers():
  return [lambda x, i=i : i * x for i in range(4)]
  
print ([m(2) for m in multipliers()])
'''

# Solution:
# [0, 2, 4, 6]
