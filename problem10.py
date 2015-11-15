import math

def isprime(n):
	if n<0:
		return False
	for i in range(2, int(math.sqrt(n)+1)):
		if n%i == 0:
			return False
	return True

primes = []

for i in range(2, 2000001):
	if isprime(i):
		primes.append(i)

print sum(primes)