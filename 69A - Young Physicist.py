n = int(input())
arr = []
x,y,z = 0,0,0
flag = False
for i in range(n):
    val = list(map(int,input().split()))
    arr.append(val)
for i in range(n):
    x = x + arr[i][0]
    y = y + arr[i][1]
    z = z + arr[i][2]
if x ==0 and y==0 and z==0:
    print('YES')
else:
    print('NO')