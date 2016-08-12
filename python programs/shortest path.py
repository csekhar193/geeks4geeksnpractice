t=input()
for i in range(0,t):
    s=raw_input()
    a=s.count('S')
    b=s.count('E')
    c=s.count('N')
    d=s.count('W')
    stri=0
    if b > d:
        y=b-d
        stri=("E"*y)
    else:
        y=d-b
        stri=("W"*y)
    
    if a > c:
        x=a-c
        stri1=("S"*x)
    else:
        x=c-a
        stri1=("N"*x)
    strin=sorted(stri+stri1)
    print("".join(map(str,strin)))