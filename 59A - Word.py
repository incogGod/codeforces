st = input()
cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s,c = 0,0
for i in range(len(st)):
    if st[i] in cap:
        c += 1
    else:
        s += 1
if c>s:
    print(st.upper())
else:
    print(st.lower())