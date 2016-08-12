for i in range(0,t):
    a=raw_input()
    s=map(str,a.split())
    c=len(s)
    l=[]
    for j in range(0,c):
        if j==0:
            r=int(s[j])
            w="{0:b}".format(r)
            l.append(w)
        elif j==1:
            x=int(s[j],2)
            l.append(x)
        elif j==2:
            y=hex(int(s[j])).split('x')[1]
            l.append(y)
        else:
            z=int(s[j],16)
            l.append(z)
    print(" ".join(map(str,l)))