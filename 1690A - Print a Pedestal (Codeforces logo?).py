for _ in range(int(input())):

    n = int(input())
    n2,n1 = int(n/3),int(n/3)
    n3 = n-n1-n2
    flag =True

    while flag:
        if n3>1 and n2<=n1:
            n1,n3 = n1+1,n3-1

        if n1>n2 and n2>n3 and n3>0 and n==n1+n2+n3:
            l2,l1,l3 = n2,n1,n3
            flag = False
        
        if n3>1 and n2+1<n1:
            n2,n3 = n2+1,n3-1

        if n1>n2 and n2>n3 and n3>0 and n==n1+n2+n3:
            l2,l1,l3 = n2,n1,n3
            flag = False
            
    print(l2,l1,l3)