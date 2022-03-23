# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.


# Version 1:
def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]


print(find_uniq([0, 0, 2, 0, 0]))


# Version 2:
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


print(find_uniq([0, 0, 0.55, 0, 0]))


def find_uniq(arr):
    return [i for i in set(arr) if arr.count(i) == 1][0]


print(find_uniq([0, 0, 1, 0, 0, 0]))
