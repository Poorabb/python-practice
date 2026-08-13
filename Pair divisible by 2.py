# Function to count pairs that sum up to even numbers

def count_even_pair(arr: list) -> int:
    _pair_count = 0
    _end = len(arr)
    for x in range(0,_end):
        for y in range(x+1,_end):
            if (arr[x] + arr[y]) % 2 == 0:
                _pair_count+=1
    return _pair_count

print(count_even_pair([1,2,3,4]))
