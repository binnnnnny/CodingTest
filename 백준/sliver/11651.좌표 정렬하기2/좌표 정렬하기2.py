import sys
N = int(sys.stdin.readline())

spots = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key = lambda x : (x[1],x[0]))
for i in spots:
    print(*i)
