import math
t = int(input())
def interesting(x):
    x = math.floor((x+1)/10)
    return x
arr = []
for i in range(t):
    val = int(input())
    arr.append(val)
for i in arr:
    print(interesting(i))
