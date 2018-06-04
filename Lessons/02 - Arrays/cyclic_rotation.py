#!environment/bin/python3
"""
An array A consisting of N integers is given.
Rotation of the array means that each element
is shifted right by one index,
and the last element of the array is moved to the first place.

The goal is to rotate array A K times;
that is, each element of A will be shifted to the right K times.

Write a function that, given an array A consisting of N integers
and an integer K, returns the array A rotated K times.
"""


def cyclic_rotation(A, K):
    """Cyclic rotation algorithm"""
    # If len(A) == 0
    if len(A) == 0:
        return A
    # If K == 0
    if K == 0:
        return A

    if len(A) == 1:
        return A
    if len(A) == 2:
        if K % 2 == 0:
            return A
        if K % 2 != 0:
            return list(reversed(A))

    for i in range(K):
        first, *middle, last = A
        A = last, first, *middle
        A = list(A)
    return A
