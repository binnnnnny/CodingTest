import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for i in range(N))
nums.sort()

# 산술평균
print(round(sum(nums)/N))
# 중앙값
print(nums[N//2])
# 최빈값
count_list = sorted(Counter(nums).items(), key=lambda x : (-x[1],x[0]))
if N == 1 :
    print(nums[0])
else :
    if count_list[0][1] != count_list[1][1] :
        print(count_list[0][0])
    else :
        print(count_list[1][0])

#범위
print(nums[-1]-nums[0])
