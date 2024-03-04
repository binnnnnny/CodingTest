a,b = map(int, input().split())
if a < b :
    a,b = b,a

def gcd(a,b) :
    if a % b == 0 :
        return b
    else :
        return gcd(b, a%b)
def lcm(a,b) :
    return (a*b) // gcd(a,b)
print(gcd(a,b))
print(lcm(a,b))


# 간단한 풀이
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
