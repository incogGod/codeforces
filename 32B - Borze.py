s = input()
zero = '.'
one = '-.'
two = '--'
while two in s:
    s=s.replace(two,'2')
while one in s:
    s=s.replace(one,'1')
while zero in s:
    s=s.replace(zero,'0')
print(s)