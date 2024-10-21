s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))

s1.update(s2)
print(s1, s2)
# union() method returns a new set whereas update() method adds item into the existing set from another set.

# intersection method prints only items that are similar to both the sets 
s3 = s1.intersection(s2)
print(s3)

# intersection_update() method updates the set with the common values
# s1.intersection_update(s2)
# print(s1)

# symmetric_difference() method return those values which are not common in both the sets
print(s1.symmetric_difference(s2))

# disjoint()
# issuperset()
# add() can add new items in the set
# remove('value') it will give an error if given value is not found
# discard('value') # it will not give an error if given value is not found
# pop() this method removes the random item from the set
# del setName it will delete the whole set
# clear() it will clear all the values from the set