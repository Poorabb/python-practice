''' A good number is a number that is divisible by the sum of its digits. For example, 18 is a good number because 1 + 8 = 9 and 18 is divisible by 9. Write a function that takes a number as input and returns True if it is a good number, and False otherwise. '''

def is_good_num(num: int) -> ['Good Number','Bad Number']:

    nums = list(str(num))

    sum = 0 
    for i in nums:
        sum += int(i)

    if num % sum == 0: 
        return ("Good Number")
    else: 
        return ("Bad Number")


print(is_good_num(84))