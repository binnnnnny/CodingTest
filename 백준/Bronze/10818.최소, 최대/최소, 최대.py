import sys

N = int(sys.stdin.readline())
lists = list(map(int,sys.stdin.readline().split()))
print(min(lists),max(lists))
