a,b = input(),input()
s = ''
for i in range(len(a)):
    if a[i] == b[i]:
        s = s+'0'
    else:
        s+='1'
print(s)
