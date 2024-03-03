N = int(input())
str_list = [input() for i in range(N)]
a = list(set(str_list)) # 중복제거

a = sorted(a) # 사전 순 정렬
a = sorted(a, key=lambda x : len(x)) # 길이 순 정렬

for i in a :
    print(i)
