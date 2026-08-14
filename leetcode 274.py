# LeetCode 274 - H-Index
#
# Given an array `citations` where citations[i] is the number of citations
# the researcher has for their i-th paper, return the researcher's h-index.
#
# The h-index is defined as the maximum value of h such that the researcher
# has published at least h papers that have each been cited at least h times.
#
# Examples
# --------
#   citations = [3, 0, 6, 1, 5]   -> 3
#     (3 papers have >= 3 citations; can't claim h=4)
#   citations = [1, 3, 1]         -> 1
#   citations = [0, 0, 0]         -> 0
#
# Constraints
# -----------
#   n == len(citations)
#   1 <= n <= 5000
#   0 <= citations[i] <= 1000
#
# Notes for your solution
# -----------------------
# - The naive O(N^2) approach: try every h from 1..n and count how many
#   papers have >= h citations. Works, but reveals the better idea:
#   sort the array descending and look for the largest h where the
#   h-th paper (1-indexed) still has >= h citations.
# - O(N log N) sort is easy. O(N) bucket-sort by citation count is also
#   doable given the small range of citations[i].
# - Edge case: all zeros -> answer is 0, not n.

citations = [0, 0, 0]
length = len(citations)
h = 0
top = max(citations)+1
for i in range(top):
    count = 0
    for j in range (length):
        if citations[j] >= i:
            count +=1
    if count >=i:
        h=i

print(h)

