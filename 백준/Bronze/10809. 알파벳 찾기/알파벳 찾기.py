S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = []
for i in alphabet :
    alphabet_list.append(i)

a = []
for i in alphabet_list :
    if i in S :
        a.append(S.index(i))
    else :
        a.append(-1)

print(*a)

# 더 간단한 풀이
s = input()

for a in range(97,123):
    print(s.find(chr(a)), end=' ')
