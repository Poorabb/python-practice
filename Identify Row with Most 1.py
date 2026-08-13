t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [input().split() for _ in range(n)]
    counts = [row.count("1") for row in matrix]
    print(counts.index(max(counts)) if max(counts) else -1)