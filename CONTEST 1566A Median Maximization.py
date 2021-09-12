t = int(input())
for i in range(t):
    n,s = map(int,input().split())
    if n == 1:
        print(s)
    elif n == 1:
        print(0)
    else:
        if n%2 ==0:
            print(s/(n/2)+1)
        else:
            print(round(s/round(n/2,0),0))
    

