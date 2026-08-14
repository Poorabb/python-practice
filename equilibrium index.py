# Equilibrium Index
#
# You are given an array of integers `nums` of length N.
#
# An INDEX i is an equilibrium index if the sum of all elements strictly
# to the left of i equals the sum of all elements strictly to the right of i.
# The element at index i itself is NOT included in either side.
#
# Formally, i is an equilibrium index iff:
#     nums[0] + nums[1] + ... + nums[i-1]   ==
#     nums[i+1] + nums[i+2] + ... + nums[N-1]
#
# Equivalently, if `total` is the sum of the whole array and `left` is the
# sum of everything before index i, then i is an equilibrium index iff:
#     2 * left + nums[i] == total
#
# If multiple equilibrium indices exist, return the LEFTMOST one.
# If no equilibrium index exists, return -1.
#
# Examples
# --------
#   nums = [1, 7, 3, 6, 5, 6]
#   index 3: left  = 1 + 7 + 3       = 11
#            right = 5 + 6           = 11   -> equilibrium
#   output: 3
#
#   nums = [1, 2, 3]
#   no index balances; output: -1
#
#   nums = [0, 0, 0, 0]
#   every index works; leftmost is 0
#
#   nums = [2, 1, -1]
#   index 0: left = 0,  right = 0    -> equilibrium
#   output: 0
#
#   nums = [1, -1, 0]
#   index 2: left = 0,  right = 0    -> equilibrium
#   output: 2
#
# Constraints
# -----------
#   1 <= N <= 10^5
#   -10^4 <= nums[i] <= 10^4
#
# Notes for your solution
# -----------------------
# - A naive O(N^2) solution (recomputing the left and right sums at every
#   index) will work for small N but is too slow for N = 10^5.
# - Think about what information you can carry forward as you walk through
#   the array, instead of re-summing from scratch each time.
# - You should be able to do this in O(N) time and O(1) extra space.

nums = [1, 7, 3, 6, 5, 6]

# for i in range(0,len(nums)):
#     if sum(nums[:i]) == sum(nums[i+1:]):
#         print("Equilibrium index: ", i)

# USING NO METHODS AND ONLY LOGIC:
total = sum(nums)
sum = 0 
for i in range(1,len(nums)):
    sum+=nums[i-1]
    if 2 * sum + nums[i] == total: 
        print("Equilibrium index: ", i)
