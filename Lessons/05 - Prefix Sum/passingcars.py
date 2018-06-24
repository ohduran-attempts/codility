"""
A non-empty array A consisting of N integers is given.
The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s or 1s: 0 represents a car traveling east, 1 represents a car traveling west.

The goal is to count passing cars.


We say that a pair of cars (P, Q),
P less than Q then less than N, and all bigger than 0, is passing
 when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function that, given a non-empty array A of N integers,
returns the number of pairs of passing cars.

The function should return -1 if the number of pairs of passing cars exceeds 1,000,000,000.

Assume that N is an integer within the range [1..100,000];
and each element of array A is an integer that can have one of the following values: 0, 1.

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).

"""


def passingcars(A):
    """
        We say that a pair of cars (P, Q),
        P less than Q then less than N, and all bigger than 0, is passing
        when P is traveling to the east and Q is traveling to the west.
    """
    EAST = 0
    WEST = 1
    MAX_PAIRED_CARS = 1000000000

    paired_cars = 0
    count_easts = 0

    for index in range(len(A)):
        if A[index] == EAST:
            count_easts += 1
        elif A[index] == WEST:
            paired_cars += count_easts
    if paired_cars > MAX_PAIRED_CARS:
        return -1
    return paired_cars
