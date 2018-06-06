"""
A non-empty array A consisting of N integers is given.
The array contains an odd number of elements,
and each element of the array can be paired
with another element that has the same value,
except for one element that is left unpaired.

Write a function that, given an array A consisting of N integers
fulfilling the above conditions,
returns the value of the unpaired element.

Assume that:

        N is an odd integer within the range [1..1,000,000];
        each element of array A is an integer within the range [1..1,000,000,000];
        all but one of the values in A occur an even number of times.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1) (not counting the storage required for input arguments).

"""

""" IMPROVE PERFORMANCE!! """


def odd_occurrences_old(A):
    """Odd Occurrences algorithm."""
    # list of unique values
    uniques = []
    for a in range(len(A)):
        if A[a] in uniques:
            uniques.remove(A[a])
        elif A[a] not in uniques:
            uniques.append(A[a])
    # assume only one of the values in A will remain
    return uniques[0]


def odd_occurrences(A):
    """Odd Occurrences algorithm."""
    uniques = {}
    for item in A:
        if item not in uniques.keys():
            uniques[item] = 1
        else:
            uniques[item] += 1
    for key in uniques.keys():
        if uniques[key] % 2 != 0:
            return key
