n = int(input())
s = input()
count = 0
l = [i for i in s]
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        count += 1
print(count)

