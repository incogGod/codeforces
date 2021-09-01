n = int(input())
arr = []
l,r =0,0
for i in range(n):
    v = list(map(int,input().split()))
    arr.append(v)
for i in range(n):
    if arr[i][0] == 1:
        l += 1
    if arr[i][1] == 1:
        r += 1
print(min(l,n-l)+min(r,n-r))
