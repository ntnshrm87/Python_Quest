# Prob 7

# Case 1
list_a = [ [] ]
print(list_a)
print(id(list_a))

# Case 2
list_a = [ [] ] * 4
print(list_a)
print(id(list_a))

# Case 3
list_a[0].append(28)
print(list_a)
print(id(list_a[0]))

# Case 4
list_a[1].append(16)
print(list_a)
print(id(list_a[1]))

# Case 5
list_a.append(26)
print(list_a)
print(id(list_a))
print(id(list_a[0]))
print(id(list_a[1]))
print(id(list_a[2]))
print(id(list_a[3]))
print(id(list_a[4]))

# Solution:
# [[]]
# 139844406923208
# [[], [], [], []]
# 139844406742600
# [[28], [28], [28], [28]]
# 139844406741960
# [[28, 16], [28, 16], [28, 16], [28, 16]]
# 139844406741960
# [[28, 16], [28, 16], [28, 16], [28, 16], 26]
# 139844406742600
# 139844406741960
# 139844406741960
# 139844406741960
# 139844406741960
# 139844405595264

# Reference:
# Here id() function can be referred to as a unique and constant
# for this object during its lifetime. We can take it as a memory
# address.
# In Case 1, we declared a list of list and id gave a unique value
# In Case 2, we multiplied the same 4 time and id came unique.
# In Case 3, a value 28 is appended to the list. The twist here
# can be seen from the output. Its due to Case 2. Actually in
# Case 2, we do not have created 4 lists but referenced the first
# one four times. To prove the same, we did Case 4 and Case 5.
# id for list_a and its similar entities is same for Case 2
# to Case 5.
