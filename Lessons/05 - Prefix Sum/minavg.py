"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q),
such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements).
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice.
To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""


def avg_min_two_slices1(A):
    length = len(A)

    P = [0] * (length)
    S = [0] * (length)

    index = length - 1

    while index >= 0:
        if index < length - 1:
            P[index] = P[index + 1] + A[index + 1]
            S[index] = A[index] + A[index + 1]

            if P[index] / (length - index) < min_avg:
                min_avg = P[index] / (length - index)
                min_index = index

        elif index == length - 1:
            P[index] = A[index]
            S[index] = A[index]
            min_avg = A[index]
            min_index = index

        index -= 1

    return min_index


def avg_min_two_slices(A):
    """
    Every slice must be of size 2 or 3, otherwise the optimal slice
    is of size 2 or 3 within that slice.

    given that items in A are always 10,000 or less,
    we implment a min_value of 10,0001 that will be override,
    and reach out to the minimum value of average in slices of
    length 2 or 3.
    """
    min_index = 0
    min_value = 10001

    for index in range(len(A) - 1):

        if (A[index] + A[index + 1]) / 2 < min_value:

            min_index = index
            min_value = (A[index] + A[index + 1]) / 2

        if index < len(A) - 2 and (A[index] + A[index + 1] + A[index + 2]) / 3 < min_value:

            min_index = index
            min_value = (A[index] + A[index + 1] + A[index + 2]) / 3

    return min_index

