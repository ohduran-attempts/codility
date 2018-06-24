"""
A DNA sequence can be represented
as a string consisting of the letters A, C, G and T,
which correspond to the types of successive nucleotides in the sequence.

Each nucleotide has an impact factor, which is an integer.
Nucleotides of types A, C, G and T
have impact factors of 1, 2, 3 and 4, respectively.

You are going to answer several queries of the form:
What is the minimal impact factor of nucleotides
contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1]
consisting of N characters. There are M queries,
which are given in non-empty arrays P and Q,
each consisting of M integers.

The K-th query (0 ≤ K < M) requires you to find
the minimal impact factor of nucleotides
contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

P[0] = 2    Q[0] = 4
This part contains nucleotides G and C (twice),
whose impact factors are 3 and 2 respectively, so the answer is 2.

P[1] = 5    Q[1] = 5
The part between positions 5 and 5 contains a single nucleotide T,
whose impact factor is 4, so the answer is 4.

P[2] = 0    Q[2] = 6
The part between positions 0 and 6 (the whole string) contains all nucleotides,
in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function solution(S, P, Q) that, given a non-empty string S consisting of N
characters and two non-empty arrays P and Q consisting of M integers,
returns an array consisting of M integers specifying
the consecutive answers to all queries.

Assume that:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P, Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.

Complexity:

        expected worst-case time complexity is O(N+M);
        expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


"""


def genomic_range_query(S, P, Q):
    nucleotids = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4,
    }
    impact = [nucleotids[char] for char in S]  # O(N) so far

    genomic_query = []
    for index in range(len(P)):
        start_position = P[index]
        end_position = Q[index] + 1  # inclusive

        query = min(impact[start_position:end_position])
        genomic_query.append(query)

    return genomic_query

