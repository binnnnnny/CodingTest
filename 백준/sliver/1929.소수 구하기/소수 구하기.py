m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: 
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)
