H,M = map(int,input().split())

if 45 < M <= 59 :
    print(H, M-45)
elif 0 <= M < 45 :
    if H-1 < 0 :
        print(H-1+24, 60+(M-45))
    elif H-1>=0 :
        print(H-1,60+(M-45))
elif M == 45 :
    print(H,0)
