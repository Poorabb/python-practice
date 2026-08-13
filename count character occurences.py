'''Count Character Occurrences
You are given two strings, str1 and str2. Your mission is to calculate the total number of occurrences of each unique character of str2 within the string str1. The task is to find the sum of occurrences of all unique characters from str2 in str1 and return this total count.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
For each test case:
The first line contains the string str1.
The second line contains the string str2.
Output Format
For each test case, output the total sum of occurrences of characters in str2 found in str1 on a new line.
'''


# Getting string 1 and 2 

str1 = str(input("Enter string 1: "))
str2 = str(input("Enter string 2: "))

 # getting unique letters into a set 
letters = set(str2)

# counting occurences 
occurences = 0
for letter  in str1:
    if letter in letters:
        occurences +=1

print(occurences)