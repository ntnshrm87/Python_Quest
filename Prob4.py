# Prob4.py

class Parent(object):
    var = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

# 1
print(Parent.var, Child1.var, Child2.var)

# 2
Child1.var = 2
print(Parent.var, Child1.var, Child2.var)

# 3
Parent.var = 3
print(Parent.var, Child1.var, Child2.var)

# 4
del Child1.var
print(Parent.var, Child1.var, Child2.var)

# Solution:
# 1 1 1
# 1 2 1
# 3 2 3
# 3 3 3

# Reference:
# Case 1 is a clear case of inheritance and all the var will
# gave the same result
# Case 2 has altered the value of var for Child1 instance
# and var being a public accessible entity shows the changes
# Case 3 has altered value of var for Parent instance and var
# being shared between Child2 and Parent as for Child1 it
# remains as 2 since its instantiation is alive
# Case 4 has deleted the instance for Child1's var, so the
# accessed value will be taken from the base class which is
# altered previously as 3
# All the cases are considering the class variables from
# dictionary of the current class or the class hierarchy
# If not found in both, it leads to an Attribute Error
