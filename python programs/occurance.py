def occurance(l,x):
    count=0
    for y in l:
        if y==x:
            count+=1
    return count
            

t=input()
for i in range(0,t):
    a=raw_input()
    b=map(int,a.split())
    c=raw_input()
    d=map(int,c.split())
    e=occurance(d,b[1])
    if e==0:
        print('-1')
    else:
        print e