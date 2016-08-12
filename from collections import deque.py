t=input()
for i in range(0,t):
    a = raw_input()
    b = map(int,a.split())
    c = raw_input()
    d = map(int,c.split())
    d.sort()
    l=[]
    for j in reversed(d):
        l.append(j)
    l1=[]
    for k in range(0,b[1]):
        l1.append(l[k])
    print(" ".join(map(str,l1)))
