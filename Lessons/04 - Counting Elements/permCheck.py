"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once,
and only once.

The goal is to check whether array A is a permutation.

Write a function that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

Assume that:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

"""


def permcheck(A):
    candidates = [False] * len(A)

    try:
        for number in A:
            if 0 < number <= len(A) and not candidates[number - 1]:
                candidates[number - 1] = True
        for boolean in candidates:
            if not boolean:
                return 0
        return 1
    except Exception:
        return 0
