t=input()
for i in range(t):
    s=raw_input()
    sum=4
    bet=1
    for i in s:
        if i=='W':
            sum+=bet
            bet=1
        else:
            sum-=bet
            bet*=2
        if sum<bet:
            break
    if sum>=bet:
        print(sum)
    else:
        print('-1')