lists = list(map(int,input().split()))

asc = [1,2,3,4,5,6,7,8]
dsc = sorted(asc,reverse=True)

if lists == asc :
    print('ascending')
elif lists == dsc :
    print('descending')
else :
    print('mixed')
