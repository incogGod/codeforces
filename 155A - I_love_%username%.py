n = int(input())
arr = list(map(int,input().split()))
count = 0
for i in range(n):
    if i == 0:
        min,max = arr[0],arr[0]
        continue
    if arr[i] > max:
        max = arr[i]
        count+=1
    if arr[i] < min:
        min = arr[i]
        count+=1
print(count)

    