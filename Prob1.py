class C:
    dangerous = 2


c1 = C()
c2 = C()
print(c1.dangerous)
c1.dangerous = 3
print(c1.dangerous)
print(c2.dangerous)
del c1.dangerous
print(c1.dangerous)
print(c2.dangerous)

# Solution:
# 2
# 3
# 2
# 2
# 2

# Reference:
# object.__del__(self)
# Called when the instance is about to be destroyed. This is also called a destructor.
# If a base class has a __del__() method, the derived class’s __del__() method,
# if any, must explicitly call it to ensure proper deletion of the base class part of the instance.
# Note that it is possible (though not recommended!) for the __del__() method to postpone destruction
# of the instance by creating a new reference to it. It may then be called at a later time when
# this new reference is deleted. It is not guaranteed that __del__() methods are called for objects
# that still exist when the interpreter exits.

# Note del x doesn’t directly call x.__del__() — the former decrements the reference count for x by one,
# and the latter is only called when x’s reference count reaches zero. Some common situations
# that may prevent the reference count of an object from going to zero include: circular references
# between objects (e.g., a doubly-linked list or a tree data structure with parent and child pointers);
# a reference to the object on the stack frame of a function that caught an exception (the traceback
# stored in sys.exc_traceback keeps the stack frame alive); or a reference to the object on the
# stack frame that raised an unhandled exception in interactive mode (the traceback stored in
# sys.last_traceback keeps the stack frame alive). The first situation can only be remedied by
# explicitly breaking the cycles; the latter two situations can be resolved by storing None in
# sys.exc_traceback or sys.last_traceback. Circular references which are garbage are detected when
# the option cycle detector is enabled (it’s on by default), but can only be cleaned up if there
# are no Python-level __del__() methods involved. Refer to the documentation for the gc module
# for more information about how __del__() methods are handled by the cycle detector,
# particularly the description of the garbage value.
