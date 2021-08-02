t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    sum = 0
    for j in range(n-1):
        sum = max(sum,arr[j] * arr[j+1])
    print(sum)