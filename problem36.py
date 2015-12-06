import math

def is_prime(n):
    if n < 0:
        return False
    for f in range(2, int(math.sqrt(n))+1):
        if n%f == 0:
            return False
    return True

def truncate(n):
	for i in range(1,len(str(n))):
		print str(n)[:i]

truncate(3797)
# Not solved. I am stupid