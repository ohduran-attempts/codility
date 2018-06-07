"""
Write a function that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N)

"""


def missinginteger(A):
    """Missing Integer challenge."""
    candidates = range(1, len(A) + 1)
    for number in A:
        if number in candidates:
            candidates.remove(number)
    if len(candidates) > 0:
        return candidates[0]
    return len(A) + 1
