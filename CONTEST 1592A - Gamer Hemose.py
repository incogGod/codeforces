for _ in range(int(input())):
    n,h = map(int,input().split())
    lst = list(map(int,input().split()))
    big,big2 = 0,0
    for i in lst:
        if i>big:
            big2 = big
            big = i
        elif i>big2:
            big2 = i
    if True:
        c = int(h/(big+big2))
        h = h - (c*(big+big2))
        count,num = 2*c,0
        while h>0:
            if num%2 == 0:
                h -= big
                count += 1
                num += 1
            else:
                h -= big2
                count += 1
                num += 1
        print(count)




