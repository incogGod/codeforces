n = int(input())
arr = []
for i in range(n):
    val = input()
    arr.append(val)
a = arr[0]
a_count = 0
b_count = 0
for i in range(n):
    if arr[i] == a:
        a_count += 1
    else:
        b = arr[i]
        b_count += 1
if b_count > a_count:
    print(b)
else:
    print(a)