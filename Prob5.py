# Prob 5

def div1(a,b):
    print("%s/%s = %s" % (a, b, a/b))

def div2(a,b):
    print("%s//%s = %s" % (a, b, a//b))

div1(3, 2)
div1(3., 2)
div1(3., 2.)
div2(3, 2)
div2(3., 2)
div2(3., 2.)

# Solution: No integer arithmetic in Python 3.
# In Python 2, 3/2 = 1 otherwise everything same

# 3/2 = 1.5
# 3.0/2 = 1.5
# 3.0/2.0 = 1.5
# 3//2 = 1
# 3.0//2 = 1.0
# 3.0//2.0 = 1.0
