word = input().upper()
alphabet = dict()

for i in word :
    if i in alphabet :
        alphabet[i]+=1
    else :
        alphabet[i]=1

# 개수 세기
cnt = 0
res = ''
for i in alphabet :
    if alphabet[i] > cnt :
        cnt = alphabet[i]
        res = i
    elif alphabet[i]==cnt :
        res = '?'
print(res)
