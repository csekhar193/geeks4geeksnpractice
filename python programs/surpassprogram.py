t=input()
for k in range(0,t):
    n=input()
    a=raw_input()
    b=map(int,a.split())
    l=len(b)
    li=[]
    for i in range(0,l):
        c=0
        for j in range(i+1,l):
            if b[j] > b[i]:
                c+=1
        li.append(c)
    print(" ".join(map(str,li)))