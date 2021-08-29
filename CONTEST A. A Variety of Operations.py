t = int(input())
for i in range(t):
    a,b = 0,0
    c,d = map(int,input().split())
    if c-d ==0:
        if c==0:
            print(0)
        else:
            print(1)    
    elif (c-d)%2 ==0:
        print(2) 
    else:
        print(-1)       