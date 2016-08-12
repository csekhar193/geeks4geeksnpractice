t=input()
for i in range(t):
    a=input()
    b=str(a)
    sum=0
    for x in b:
        c=int(x)
        sum+=c
    if a%sum==0:
        print '1'
    else:
        print '0'