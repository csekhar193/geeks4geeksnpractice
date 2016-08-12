from collections import Counter
t = input()
for i in range(0,t):
    a= input()
    b="{0:b}".format(a)
    c=str(b)
    counter = Counter(c)
    b=counter['1']
    if b==1:
        d=c[::-1]
        e=d.index('1')
        print(e+1)
    else:
        print('-1')