while True :
    cases = input()
    if cases == '0' or cases[0]==0 :
        break
    else :
        n = len(cases)//2
        sum = 0
        for i in range(n) :
            if cases[i] != cases[-(i+1)] :
                print('no')
                break
            else :
                sum += 1
        if sum == n :
            print('yes')

# 더 쉬운 풀이
while True :
  cases = input()
  if cases == "0" :
      break

answer = 'no"
if cases == cases[::-1] :
    answer = 'yes'

print(answer)
