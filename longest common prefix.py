'''Longest Common Prefix
You are given a list of strings str
str. Your task is to find the longest common prefix among all the strings in the list. If there is no common prefix, return -1.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two lines of input:
The first line contains an integer N, the number of strings.
The next line contain a string array str.
Output Format
For each test case, output the longest common prefix. If there is no common prefix, output -1.'''

str = "flower flow flight"
list_of_words = str.split()
first = list_of_words[1]
print(first)
letters = list(first)
print(letters)
comp = '' 
for i in letters:
    new = comp + i
    pre = True 
    for j in list_of_words: 
        if j.startswith(new):
            continue
        else:
            pre = False
            break
    if pre:
        comp = new
    else:
        break
    
print(comp)