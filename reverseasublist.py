def reverse_sublist(lst,start,end):
    lst[start:end] = lst[start:end][::-1]
    return lst
    
t=input()
for i in range(t):
    n=input()
    a=raw_input()
    b=map(int,a.split())
    i=raw_input()
    i1=map(int,i.split())
    x=i1[0]-1
    y=i1[1]
    z=reverse_sublist(b,x,y)
    print(" ".join(map(str,z)))