a = input()
if len(a) == 1:
    print(a)
else:
    arr = a.split('+')
    arr.sort()
    a = '+'.join(arr)
    print(a)
