A = int(input())
B = int(input())
C = int(input())
num = str(A * B * C)
nums = dict()

for i in range(len(num)) :
    if num[i] not in nums :
        nums[num[i]] = 1
    else :
        nums[num[i]] += 1

for i in range(10) :
    if str(i) not in nums :
        print(0)
    else :
        print(nums[str(i)])
