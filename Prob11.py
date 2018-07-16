# Find the product of array/list indices except the specific index with improved time complexity.
# e.g. 
# Input: [1, 7, 3, 2]
# Output: [42, 6, 14, 21]

import time
import random
import numpy

# Input
x = [random.randrange(1, 10, 1) for _ in range(10)]

l1 = []
tmp = 1
y = 1

# Case 1: With O(n^2) complexity
start = time.time()
for i in range(0,len(x)):
    for j in range(0, len(x)):
        if i != j:
            y = y * x[j]
    l1.append(y)
    y = 1
print str(l1) + ' has taken ' + str(time.time() - start)

# Case 2: With O(n) complexity
start = time.time()
l = numpy.ones(10, int)
for i in range(0,len(x)):
    l[i] = tmp
    tmp *= x[i]

tmp = 1

for i in reversed(range(0,len(x))):
    l[i] *= tmp
    tmp *= x[i]
print str(l) + ' has taken ' + str(time.time() - start)

# Sample Output for 10 elements array:
# [784000, 784000, 392000, 627200, 448000, 627200, 627200, 448000, 3136000, 784000] has taken 2.90870666504e-05
# [784000  784000  392000  627200  448000  627200  627200  448000 3136000 784000] has taken 0.000211000442505
