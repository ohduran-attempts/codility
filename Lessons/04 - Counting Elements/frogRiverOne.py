"""
A small frog wants to get to the other side of a river.
The frog is initially located on one bank of the river (position 0)
and wants to get to the opposite bank (position X+1).
Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves.
A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river.
The frog can cross only when leaves appear at every position across the river from 1 to X
(that is, we want to find the earliest moment when all the positions from 1 to X
are covered by leaves).

You may assume that the speed of the current in the river is negligibly small,
i.e. the leaves do not change their positions once they fall in the river.

Write a function that, given a non-empty array A
consisting of N integers and integer X,
returns the earliest time when the frog
can jump to the other side of the river.
"""


def frogriverone(X, A):
    """Solve frogRiverOne challenge."""
    if X > max(A):
        return -1
    if len(A) == 0:
        return -1
    uniques = [x for x in range(1, X + 1)]
    i = 0
    while len(uniques) > 0 and len(uniques) <= i or i < len(A):
        if A[i] in uniques:
            uniques.remove(A[i])
        if len(uniques) == 0:
            return i
        i += 1
    return -1

print(frogriverone(2, [2, 2, 2, 2, 2]))
