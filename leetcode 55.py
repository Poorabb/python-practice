# LeetCode 55 - Jump Game
#
# You are given an integer array `nums`. You are initially positioned at the
# first index, and each element `nums[i]` represents the maximum jump length
# you can take from position i.
#
# Return True if you can reach the last index, or False otherwise.
#
# Examples
# --------
#   nums = [2, 3, 1, 1, 4]   -> True
#   nums = [3, 2, 1, 0, 4]   -> False
#
# Constraints
# -----------
#   1 <= len(nums) <= 10^4
#   0 <= nums[i] <= 10^5
#
# Notes for your solution
# -----------------------
# - A reachable index lets you reach any index in the range
#   [i, i + nums[i]]. Think about what state you'd carry as you walk
#   left-to-right to know "is index k reachable?" in O(1).
# - O(N) time and O(1) extra space is straightforward.
# - Greedy works: track the farthest index you can reach so far.

nums = [2, 3, 1, 1, 4]
current_index = 0
print(len(nums))
win = False
while current_index < len(nums):
    if current_index != len(nums)-1:
        if nums[current_index] == 0:
            win = False
            break
        else:
            current_index += nums[current_index]
    else: 
        win = True 
        break

print(win)

#have to do 