t=input()
for i in range(0,t):
    a=raw_input()
    b=raw_input()
    for char in b:
        a = a.replace(char,"")
    print a