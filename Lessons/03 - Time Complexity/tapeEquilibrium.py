#!environment/bin/python3
"""
A non-empty array A consisting of N integers is given.
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into
two non-empty parts:
The difference between the two parts is the absolute difference
between the sum of the first part and the sum of the second part.

Write a function that, given a non-empty array A of N integers,
returns the minimal difference that can be achieved.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N)
"""


def tapeequilibrium(A):
    """Tape Equilibrium."""
    left = A[0]
    right = sum(A[1:])
    candidate = abs(left - right)
    for index in range(1, len(A) - 1):
        left += A[index]
        right -= A[index]
        candidate = min(candidate, abs(left - right))
    return candidate
