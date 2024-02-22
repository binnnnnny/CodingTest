# 처음 푼 풀이
num_list = [int(input()) for i in range(9)]

max_num = 0
res = ''
for i in range(9) :
    if max_num < num_list[i] :
        max_num = num_list[i]
        res = i+1
print(max_num)
print(res)

# 더 간단한 풀이
num = [int(input()) for i in range(9)]

print(max(num))
print(num.index(max(num)))
