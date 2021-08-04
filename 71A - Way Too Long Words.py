t = int(input())
for i in range(t):
    val = input()
    if len(val) > 10:
        print(val[0]+str(len(val)-2)+val[-1])
    else:
        print(val)