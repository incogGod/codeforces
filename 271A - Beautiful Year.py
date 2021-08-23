y = int(input())
flag = True
while flag:
    y += 1
    if not (str(y)[0] == str(y)[1] or str(y)[0] == str(y)[2] or str(y)[0] == str(y)[3]):
        if not (str(y)[1] == str(y)[2] or str(y)[1] == str(y)[3]):
            if not (str(y)[2] == str(y)[3]):
                flag = False
print(y)