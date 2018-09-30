myFavSet = {1, 2, 3, 4, 5,}
print(myFavSet)
myFavSet.add(6)
print(myFavSet)
myFavSet.update([7, 9, 10, 11])
print(myFavSet)
#   we can't have a duplicate value in a set. If we have any element two times than
#   than the second element gets neglected.
myFavSet.remove(7)
print(myFavSet)
myFavSet.discard(12)
print(myFavSet)