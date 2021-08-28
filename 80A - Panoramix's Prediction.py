n,m = map(int,input().split())
def isprime(num):
    for j in range(2,int((num/2)+1)):
        if num%j ==0:
            return False
            break
    return True
flag = False
for i in range(n+1,m+1):
    if isprime(i):
        if i ==m:
            print('YES')
            flag = True
            break
        else:
            print('NO')
            flag = True
            break

if flag == False:
    print('NO')

