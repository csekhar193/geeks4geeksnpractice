t=input()
for i in range(0,t):
    a=input()
    b=raw_input()
    c=map(int,b.split())
    ans=0
    for j in range(0,a):
        for k in range(j+1,a):
            ans+=c[j]&c[k]
    print ans