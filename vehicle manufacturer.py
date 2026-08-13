'''Vehicle Manufacturing
You are tasked with determining the number of two-wheelers and four-wheelers that need to be manufactured based on the given total number of vehicles and the total number of wheels.

You are provided with two integers:

v: the total number of vehicles (both two-wheelers and four-wheelers).
w: the total number of wheels for all the vehicles combined.
Your task is to calculate and print how many two-wheelers and four-wheelers must be manufactured based on the input data. If it's not possible to manufacture such a combination, print 
-1.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line contains an integer 
v
v — the total number of vehicles.
The second line contains an integer 
w
w — the total number of wheels.
Output Format
For each test case,

If a valid combination of two-wheelers and four-wheelers exists, print two integers:
The number of two-wheelers, the number of four-wheelers.
If no valid combination is possible, print -1.
Constraints'''


vehicle_count = int(input("Enter Vehicle count:  "))
tire_count = int(input("Enter tire count:  "))

ini_pointer = 0 
final_pointer = vehicle_count

while ini_pointer < vehicle_count: 
    if (ini_pointer * 4) + (final_pointer * 2) == tire_count:
        print ("Four wheelers: ",ini_pointer,"Two wheelers: ",final_pointer)
        exit()
    else:
        ini_pointer += 1
        final_pointer -= 1
    
print('-1')

    
     

