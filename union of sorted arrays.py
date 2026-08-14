# Union of Sorted Arrays
#
# You are given two sorted arrays, arr1 and arr2.
# Your task is to find the union of these two arrays.
# The union includes all distinct elements from both arrays in ascending order.
#
# Write a function that returns the union of arr1 and arr2 in a single sorted array.
#
# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of two lines of input:
#   The first line contains two integers N and M, denoting the size of the two arrays.
#   The next two lines denote the two arrays arr1 and arr2 of size N and M respectively.
#
# Output Format
# For each test case, output a sorted array containing the distinct elements
# from both arr1 and arr2.

arr1 = [1,3,4,5,7]
arr2 = [2,3,5,10]

result_arr = []  


pointer1 = 0 
pointer2 = 0

while pointer1 < len(arr1) and pointer2 < len(arr2):
    if arr1[pointer1] < arr2[pointer2]:
        result_arr.append(arr1[pointer1])
        pointer1+=1
    elif arr1[pointer1] > arr2[pointer2]:
        result_arr.append(arr2[pointer2])
        pointer2+=1
    else:
        result_arr.append(arr1[pointer1])
        pointer1+=1
        pointer2+=1

result_arr.extend(arr1[pointer1:])
result_arr.extend(arr2[pointer2:])

print(set(result_arr))