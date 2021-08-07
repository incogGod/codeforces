s = input()
s = s.lower()
k = ''
lst = ['a','e','i','o','u','y']
for i in range(len(s)):
    if s[i] not in lst:
        k = k+'.'
        k = k+s[i]
print(k)