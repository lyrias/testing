import math
def fibonacci(n):
    x, y, z = 1, 1, 1
    while z<n:
        x, y = y, y + x
        z=z+1
    pass
    return x
n=1
while n>0:
	n = int(input(""))
	salt = 4
	for x in xrange(1,n+1):
		if x%4==0:
			print fibonacci(salt)

			salt=salt+4
	pass
pass
