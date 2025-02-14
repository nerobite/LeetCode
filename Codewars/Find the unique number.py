"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.
"""
def find_uniq(arr):
    arr = sorted(arr)
    n = arr[0] if arr[0] != arr[-1] and arr[-1] == arr[-2] else arr[-1]
    return n