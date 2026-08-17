def longest_consecutive(nums):
    """
    Returns the length of the longest consecutive elements sequence.
    Runs in O(n) time using a hash set.

    Trick: only start counting from a number that is the beginning
    of a sequence (i.e., num - 1 is not in the set). This ensures
    each number is visited at most once across all inner loops.
    """
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if 'num' is the start of a sequence
        if num - 1 not in num_set:
            length = 1
            current = num
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    # Test cases
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))           # 4
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 9
    print(longest_consecutive([1, 0, 1, 2]))                   # 3
    print(longest_consecutive([]))                             # 0
    print(longest_consecutive([1]))                            # 1
    print(longest_consecutive([1, 2, 0, 1]))                   # 3
