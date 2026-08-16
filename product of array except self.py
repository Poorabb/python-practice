# LeetCode 238: Product of Array Except Self
# Medium
#
# Given an integer array nums, return an array answer such that answer[i] is equal
# to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Example 1:
#   Input: nums = [1,2,3,4]
#   Output: [24,12,8,6]
#
# Example 2:
#   Input: nums = [-1,1,0,-3,3]
#   Output: [0,0,9,0,0]
import math 


# THIS CODE WORKS BUT HAS A COMPLEXITY OF O(n^2)
nums = [1,2,3,4]
# result = []

# # print(math.prod(nums[:2]))
# for i in range (len(nums)):
#     result.append(math.prod(nums[:i])*math.prod(nums[i+1:]))
# print(result)


# CODE FOR O(n) COMPLEXITY
prod_ltr = []
prod_rtl = []
prod = 1 
for i in range(len(nums)):
    if i == 0: 
        prod_ltr.append(1)
    else:
        prod_ltr.append(prod*nums[i-1])
        prod = prod*nums[i-1]

print(prod_ltr)

prod = 1 
for i in range(len(nums)-1,-1,-1):
    if i == len(nums)-1: 
        prod_rtl.append(1)
    else:
        prod_rtl.append(prod*nums[i+1])
        prod = prod*nums[i+1]

print(prod_rtl)

ltr_pointer=0 
rtl_pointer=len(nums)-1
answer = []

for i in range(len(nums)):
    answer.append(prod_ltr[ltr_pointer]*prod_rtl[rtl_pointer])
    ltr_pointer+=1 
    rtl_pointer-=1
print(answer)

