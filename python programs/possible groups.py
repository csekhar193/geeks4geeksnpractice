from itertools import permutations
a=[3, 6, 7, 2, 9]
b=list(permutations(a))
c=len(b)
for i in range(0,c):
	if b[i]/3:
		print b