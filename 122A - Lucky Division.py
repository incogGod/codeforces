n = int(input())
l = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
flag = False
for i in l:
    if n== 0:
        print('NO')
        flag = True
    else:
        if n % i == 0:
            print('YES')
            flag = True
            break
if flag == False:
    print('NO')
