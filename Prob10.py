x1 = [10,4,10,8,13,11,10,23,11,23,24,11]

x = sorted(x1)
print (x)  # [4, 4, 8, 10, 10, 10, 11, 11, 11, 13, 23]

# To find the duplicate elements in the list
print "Getting duplicate elements... "
for i in range(len(x)-1):
    if x[i] == x[i+1] :
        i += 1
    else:
        print (x[i])

if x[len(x)-1] != x[len(x)-2]:
    print (x[len(x)-1])

print "\n"

# To find the unique non repetitive elements in the list
print "Getting unique no repeating elements... "
for i in range(len(x)-1):
    if x[i] == x[i+1]:
        i += 1
    else:
        if x[i] == x[i-1]:
            pass
        else:
            print (x[i])

if x[len(x)-1] != x[len(x)-2]:
    print (x[len(x)-1])

print "\n"

# To find the first repeating element from the list
for i in range(0,len(x1)-1):
    for j in reversed(range(0,len(x1)-1)):
        if x1[i] == x1[j]:
            print "First repeating element is: ",x1[i]
            break
    break


