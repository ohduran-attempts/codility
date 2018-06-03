"""
BINARY GAP:
A binary gap within a positive integer N is any maximal sequence of consecutive zeros
that is surrounded by ones at both ends in the binary representation of N.

Write a function that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
"""


def binary_gap(N=0):
    """
    Binary Gap
    Complexity:

            expected worst-case time complexity is O(log(N));
            expected worst-case space complexity is O(1).
    """
    # Capture exceptions
    if not isinstance(N, int):
        raise Exception
    if N < 0:
        raise Exception
    # Convert N to binary string
    binary_string = "{0:b}".format(N)
    # Loop through the string and record the largest gap.
    gap = 0
    current_gap = 0
    for s in binary_string:
        if s == '0':
            current_gap += 1
        else:
            gap = max(gap, current_gap)
            current_gap = 0

    return gap
