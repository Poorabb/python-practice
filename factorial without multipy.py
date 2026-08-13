# CREATE A FUNCTION FOR MULTIPLY SO THAT WE DONT HAVE TO USE THE OPERATOR 
def multiply(a:int, b:int) -> int:
    sum = 0
    for i in range(b):
        sum +=a
    return sum

print(multiply(5,10))

def fact(num: int) -> int:
    if num <= 1:
        return 1
    return multiply(num,fact(num-1))


print(fact(5))
