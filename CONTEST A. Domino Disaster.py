t = int(input())
for test in range(t):
    n = int(input())
    s = input()
    x = ''
    for i in range(n):
        if s[i] == 'L':
            x = x + 'L'
        elif  s[i] == 'R':
            x += 'R'
        elif s[i] == 'U':
            x += 'D'
        elif s[i] ==  'D':
            x += 'U'
    print(x)