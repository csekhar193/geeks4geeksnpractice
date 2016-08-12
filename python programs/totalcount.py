t=input()
for i in range(0,t):
    a=raw_input()
    b=map(int,a.split())
    c=raw_input()
    d=map(int,c.split())
    e=len(d)
    count=0
    for j in range(0,e):
        if d[j]%b[1]==0:
            f=d[j]/b[1]
            count=count+f
        else:
            g=d[j]/b[1]
            count=count+g+1
        
    print(count)