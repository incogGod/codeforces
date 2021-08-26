count,n,flag = 0 ,int(input()),False
for i in str(n):
    if (i == '4' or i == '7'):
        count += 1
for i in str(count):
    if not(i == '4' or i == '7'):
        flag = True
print('YES') if flag == False else print('NO')