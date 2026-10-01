my_set = {1,2,3,4}
my_set.add(5)
my_set.add(6)

my_set.remove(3)
my_set.pop()


my_set.add(10)
print(my_set)


set1 = {2,3,12,45,789,2234,125}
set2 = {2,1,5,233,125,2134,276}

union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)

difference_1 = set1-set2
print(difference_1)

difference_2 = set2-set1
print(difference_2)
