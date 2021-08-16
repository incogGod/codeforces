n,m = map(int,input().split())
while not n ==0 and not m ==0 :
    n,m = n - 1,m - 1
    if n ==0 or m ==0:
        print('Akshat')
        break
    n,m = n - 1,m - 1
    if n ==0 or m ==0:
        print('Malvika')
        break       