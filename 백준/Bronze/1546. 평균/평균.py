import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
M = max(nums)
print(sum(nums)*100/M/N)
