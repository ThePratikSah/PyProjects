set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8, 9}
print(set1 | set2)  # set union gives all the element present in set1 and set2
# and neglecting the duplicate element.

print(set1 & set2)  #set intersection gives the element that are common
# in both the set.
print(set1 - set2)  #set difference of set1 and set2 gives set1.
print(set2 - set1)  #set difference of set2 and set1 gives set2.

print(set1 ^ set2)  # symmetric difference of set1 and set2 is a set of element .
#   set1 and set2 both except those that are common in both.


