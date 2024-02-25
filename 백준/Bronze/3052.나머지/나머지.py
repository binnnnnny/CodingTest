nums = [int(input()) for i in range(10)]
ab = dict()

c = 0
for i in nums :
    c = i%42
    if c not in ab :
        ab[c] = 1
    else :
        ab[c] += 1

print(len(ab.keys()))
