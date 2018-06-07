"""
You are given N counters, initially set to 0,
and you have two possible operations on them:

increaseX: counter X is increased by 1
max counter: all counters set to the max value of the counter list.

A non-empty array A of M integers is given.
This array represents consecutive operations:

if A[K] = X, such that X is less than N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.

The goal is to calculate the value of every counter after all operations.

Write a function that, given an integer N and a non-empty array A consisting of M integers,
returns a sequence of integers representing the values of the counters.
The sequence should be returned as an array of integers.

Assume that:

        N and M are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..N + 1].

Complexity:

        expected worst-case time complexity is O(N+M);
        expected worst-case space complexity is O(N).


"""


def maxcounters(N, A):
    """Implement Max Counter Challenge."""
    counters = [0] * N
    max_counter_code = N + 1
    max_value = 0

    for operation_code in A:
        if operation_code != max_counter_code:
            counters[operation_code - 1] += 1
            max_value = max(max_value, counters[operation_code - 1])
        if operation_code == max_counter_code:
            counters = [max_value] * N
    return counters
