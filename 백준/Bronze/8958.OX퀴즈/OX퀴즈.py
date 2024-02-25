n = int(input())
for i in range(n) :
    ox = list(map(str,input()))
    o = 0
    score = 0
    for j in range(len(ox)) :
        if ox[j] == 'O' :
            o += 1
            score += o
        else :
            o = 0
    print(score)
