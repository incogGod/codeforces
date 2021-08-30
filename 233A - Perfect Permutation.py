n = int(input())
even,odd,s =0,1,''
if n%2==1:
    print(-1)
    
else:
    for i in range(1,n+1):
        if i%2 !=0:
            even = even + 2 
            s+=' '+str(even)
        else:
            if i==2:
                s+= ' '+str(odd)
            else:
                odd+= 2
                s+=' '+str(odd)
    print(s[1:])
