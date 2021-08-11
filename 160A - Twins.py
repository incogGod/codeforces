n = int(input())
coins = list(map(int,input().split()))
coins.sort(reverse=True)
sum1 = 0
c =sum(coins)
for i in range(n):
    sum1 = sum1 + coins[i]
    if sum1 > (c-sum1):
        print(i+1)
        break

