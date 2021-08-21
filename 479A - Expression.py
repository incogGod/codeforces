a,b,c = int(input()),int(input()),int(input())
lst = [(a+b+c),(a+b)*c,a+b*c,a*b+c,a*(b+c),a*b*c]
print(max(lst))