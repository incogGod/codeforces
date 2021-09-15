import math
t = int(input())
for i in range(t):
    n,s = map(int,input().split())
    if n == 1:
        print(s)
    elif n ==2:
        print(math.floor(s/n))
    elif n%2 ==0:
        print(math.floor(s/(1+(n/2))))
    else:
        print(math.floor(s/math.ceil(n/2)))