n = int(input())
teams = []
count = 0
for i in range(n):
    val = list(map(int,input().split()))
    teams.append(val)
for i in range(n):
    for j in range(n):
        if teams[i][0] == teams[j][1]:
            count += 1
print(count)
