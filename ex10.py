t=input()
for i in range(0,t):
    a=input()
    l=[]
    for j in range(1,a+1):
        b="{0:b}".format(j)
        l.append(b)
    print(" ".join(map(str,l)))