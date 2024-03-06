import sys

N = int(sys.stdin.readline())
num = 1
result = []
for i in range(N) :
    age, name = sys.stdin.readline().split()
    result.append([int(age), name, num])
    num += 1
result = sorted(result, key=lambda x : (x[0],x[2]))

for i in range(len(result)) :
    print(*result[i][:2])
