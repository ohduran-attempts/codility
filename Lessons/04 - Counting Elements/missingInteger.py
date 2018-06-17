"""
Write a function that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N)

"""


def missinginteger_1(A):
    """Missing Integer challenge."""
    candidates = [x for x in range(1, len(A) + 1)]
    for number in A:
        if number in candidates:
            candidates.remove(number)
    if len(candidates) > 0:
        return candidates[0]
    return len(A) + 1

def missinginteger(A):
    # Indeces are 1 to len(A) - 1... what if they are negative.
    candidates = [False] * len(A)

    for i, item in enumerate(A):
        if not candidates[i - 1]:
            candidates[i - 1] = True

    for i, bool in enumerate(candidates):
        if not bool:
            return i
    return 1