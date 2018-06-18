"""
Write a function that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N)

"""


def missinginteger(A):
    candidates = [False] * (len(A) + 1)

    for item in A:
        if 0 < item <= len(A) and not candidates[item - 1]:
            candidates[item - 1] = True

    for index, boolean in enumerate(candidates):
        if not boolean:
            return index + 1
